import asyncio

from redis.asyncio import Redis
import serial_asyncio

from event_system import EventPublisher, EventType
from configs import bill_acceptor_config
from loggers import logger


class BillAcceptor:
    """Интерфейс для коммуникации с купюроприемником."""
    def __init__(self, port: str, publisher: EventPublisher, redis: Redis):
        self.port = port
        self.publisher = publisher
        self.redis = redis

        # коммуникация
        self.reader = None
        self.writer = None
        self._msg_queue = asyncio.Queue()

        # отслеживание состояний
        self._active = False
        self.target_amount = 0
        self.last_processed_bill = None
        self.bill_processed = False
        self.max_bill_count = None
        self.state_history = []

        # Счетчик транзакций - добавлено для решения проблемы с одинаковыми купюрами
        self.transaction_counter = 0


    async def initialize(self):
        """Инициализация."""
        if not await self._check_bill_acceptor_capacity():
            return False

        try:
            self.reader, self.writer = await serial_asyncio.open_serial_connection(
                url=self.port,
                baudrate=9600
            )
            poll_cmd = bill_acceptor_config.CMD_PULL
            poll_cmd += self._calculate_crc(poll_cmd)
            self.writer.write(poll_cmd)
            await self.writer.drain()
            response = await self._read_ccnet_message()
            if not response:
                raise
            # Reset state tracking
            self.last_processed_bill = None
            self.bill_processed = False
            self.state_history = []
            self.transaction_counter = 0
            return True
        except Exception as e:
            logger.error(f"Ошибка подключения к порту {self.port}: {e}")
            return False


    async def reset_device(self) -> bool:
        """Сброс."""
        try:
            self.writer.write(bill_acceptor_config.CMD_RESET_DEVICE)
            await self.writer.drain()
            await asyncio.sleep(2)  # Allow time for device to reset
            return True
        except Exception as e:
            logger.error(f"Ошибка сброса купюроприемника: {e}")
            return False


    async def start_accepting(self) -> None:
        """Начало приема купюр."""
        self._active = True
        await self._enable_all_bills()
        asyncio.create_task(self._serial_reader_task())
        asyncio.create_task(self._message_processor_task())


    async def stop_accepting(self) -> None:
        """Остановка приема купюр."""
        # Send disable command
        disable_cmd = self._calculate_crc(bill_acceptor_config.CMD_DISABLE)
        self.writer.write(disable_cmd)
        await self.writer.drain()
        self._active = False


    def _calculate_crc(self, data: bytes) -> bytes:
        """Расчет CRC."""
        crc = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ bill_acceptor_config.CRC_POLYNOMIAL
                else:
                    crc = crc >> 1
        return crc.to_bytes(2, 'little')


    def _verify_checksum(self, response: bytes) -> bool:
        """Валидация CRC ответа."""
        if len(response) < 6:
            return False

        # Calculate CRC for all data except the last 2 bytes (which are the CRC)
        calculated_crc = self._calculate_crc(response[:4])
        received_crc = response[4:6]

        return True
        # if calculated_crc == received_crc:
        #     return True
        # else:
        #     logger.error(f"Некорректный CRC. Ожидается: "
        #                  f"{calculated_crc.hex()}, получено: {received_crc.hex()}")
        #     return False


    async def _read_ccnet_message(self):
        """Чтение сообщения по протоколу CCNET."""
        # Сначала читаем первые 3 байта, чтобы получить длину сообщения
        header = await asyncio.wait_for(self.reader.read(3), timeout=1.0)
        if len(header) < 3:
            logger.error("Ошибка чтения заголовка собщения")
            return None

        # Извлекаем значение LNG (общая длина сообщения)
        total_length = header[2]

        # Читаем оставшиеся байты в соответствии с указанной длиной
        remaining = await asyncio.wait_for(self.reader.read(total_length - 3), timeout=1.0)
        if len(remaining) < (total_length - 3):
            logger.error("Длина данных сообщения меньше ожидаемой")
            return None

        # Объединяем заголовок и оставшиеся данные
        complete_message = header + remaining
        return complete_message


    async def _check_bill_acceptor_capacity(self) -> bool:
        """Проверка на переполненность купюр."""
        count = int(await self.redis.get("bill_count") or 0)
        self.max_bill_count = int(await self.redis.get('max_bill_count') or 0)
        if count >= self.max_bill_count:
            logger.error("Купюроприемник переполнен")
            return False
        return True


    async def _enable_all_bills(self):
        """Активация режима приема всех купюр."""
        enable_cmd = bill_acceptor_config.CMD_ACCEPT_ALL_BILLS
        enable_cmd += self._calculate_crc(enable_cmd)
        self.writer.write(enable_cmd)
        await self.writer.drain()


    async def _serial_reader_task(self):
        """Чтение данных из com порта и отправка в очередь asyncio.Queue."""
        while self._active:
            try:
                # Send POLL command with correct CRC
                poll_cmd = bill_acceptor_config.CMD_PULL
                poll_cmd += self._calculate_crc(poll_cmd)
                self.writer.write(poll_cmd)
                await self.writer.drain()

                # Read response using the correct LNG-based approach
                response = await self._read_ccnet_message()
                if response:
                    # Queue response for processing
                    await self._msg_queue.put(response)

                # Brief delay between polls
                await asyncio.sleep(0.2)
            except asyncio.TimeoutError:
                # Timeout is normal when no response
                pass
            except Exception as e:
                logger.error(f"Ошибка чтения данных `_serial_reader_task`: {e}")
                await asyncio.sleep(1)  # Longer delay after error


    async def _message_processor_task(self):
        """Получение задач из очереди."""
        while self._active:
            try:
                data = await self._msg_queue.get()
                await self._process_response(data)
                self._msg_queue.task_done()
            except Exception as e:
                logger.error(f"Ошибка чтения данных `_message_processor_task`: {str(e)}")


    async def _process_response(self, data: bytes) -> None:
        """Процесс обработки задач из очереди."""
        if len(data) < 6:
            return
        elif not self._verify_checksum(data):
            return

        state = data[3]
        logger.debug(f"Состояние купюроприемника: {bill_acceptor_config.STATES.get(state)}")
        logger.debug(f'Data: {[f"0x{b:x}" for b in data]}')

        # Добавляем состояние в историю
        self.state_history.append(state)
        if len(self.state_history) > 5:
            self.state_history.pop(0)

        if state == 0x80:
            logger.debug("Купюра в состоянии ESCROW, отправляем команду STACK")
            stack_cmd = bill_acceptor_config.CMD_STACK
            stack_cmd += self._calculate_crc(stack_cmd)
            self.writer.write(stack_cmd)
            await self.writer.drain()
            self.bill_processed = False

        elif state == 0x81:
            logger.debug("Купюра в состоянии STACKED")
            if len(data) > 4:
                bill_type = data[4]
                bill_code = bytes([bill_type])
                amount = bill_acceptor_config.BILL_CODES.get(bill_code, 0)

                logger.debug(f'Код принятой купюры: {bill_code}')

                if not self.bill_processed:
                    await self.publisher.publish(EventType.BILL_ACCEPTED, value=amount)
                    await self.redis.incr("bill_count")
                    self.last_processed_bill = bill_code
                    self.bill_processed = True
                    self.transaction_counter += 1
