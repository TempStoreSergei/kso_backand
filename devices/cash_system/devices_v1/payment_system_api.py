import asyncio

from devices.coin_acceptor.index import SSP
from devices.bill_acceptor.bill_acceptor import BillAcceptor
from event_system import EventPublisher, EventConsumer, EventType
from configs import PORT_OPTIONS, BILL_DISPENSER_PORT, bill_acceptor_config, \
    COIN_ACCEPTOR_PORT, MIN_BOX_COUNT
from devices.bill_dispenser.bill_dispenser import Clcdm2000, LcdmException
from loggers import logger
from redis_error_handler import redis_error_handler
from send_to_ws import send_to_ws


class PaymentSystemAPI:
    """Api для взаимодействия с наличной системой оплаты."""
    def __init__(self, redis):
        # Event system
        self.event_queue = asyncio.Queue()
        self.event_publisher = EventPublisher(self.event_queue)
        self.event_consumer = EventConsumer(self.event_queue)

        # Redis connection
        self.redis = redis

        # Devices instances
        self.hopper = SSP(self.event_publisher)
        self.bill_acceptor = BillAcceptor(
            bill_acceptor_config.BILL_ACCEPTOR_PORT,
            self.event_publisher,
            self.redis,
        )
        self.bill_dispenser = Clcdm2000()

        # Payment tracking
        self.target_amount = 0
        self.collected_amount = 0
        self.active_devices = set()
        self.is_payment_in_progress = False

        # Bill dispenser configurations
        self.upper_box_value = None
        self.lower_box_value = None
        self.upper_box_count = None
        self.lower_box_count = None


    async def bill_acceptor_status(self):
        """Статус купюроприемника."""
        try:
            max_bill_count = await self.redis.get('max_bill_count')
            bill_count = await self.redis.get('bill_count')
            return {
                'success': True,
                'message': 'Статус купюроприемника получен успешно',
                'data': {
                    'max_bill_count': int(max_bill_count) if max_bill_count else 0,
                    'bill_count': int(bill_count) if bill_count else 0,
                }
            }
        except (ConnectionError, TimeoutError) as e:
            logger.error(f"Redis connection issue: {e}")
            return {
                'success': False,
                'message': f"Redis connection issue: {e}"
            }


    async def bill_dispenser_status(self):
        """Статус купюродиспенсера."""
        try:
            upper_box_value = await self.redis.get('bill_dispenser:upper_lvl')
            lower_box_value = await self.redis.get('bill_dispenser:lower_lvl')
            upper_box_count = await self.redis.get('bill_dispenser:upper_count')
            lower_box_count = await self.redis.get('bill_dispenser:lower_count')
            return {
                'success': True,
                'message': 'Статус купюродиспенсера получен успешно',
                'data': {
                    'upper_box_value': int(upper_box_value) * 100,
                    'lower_box_value': int(lower_box_value) * 100,
                    'upper_box_count': int(upper_box_count),
                    'lower_box_count': int(lower_box_count),
                }
            }
        except (ConnectionError, TimeoutError) as e:
            logger.error(f"Redis connection issue: {e}")
            return {
                'success': False,
                'message': f"Redis connection issue: {e}"
            }


    @redis_error_handler("Максимальное количество купюр установлено успешно")
    async def bill_acceptor_set_max_bill_count(self, value: int):
        """Установка максимального количества купюр."""
        await self.redis.set('max_bill_count', value)
        await self.init_bill_acceptor()


    @redis_error_handler("Количество купюр в купюроприемнике обнулено успешно")
    async def bill_acceptor_reset_bill_count(self):
        """Сброс количества купюр в купюроприемнике (инкасация)."""
        await self.redis.set('bill_count', 0)


    @redis_error_handler("Номиналы диспенсера купюр установлены успешно")
    async def set_bill_dispenser_lvl(self, upper_lvl, lower_lvl):
        """Установка номиналов купюр в диспенсере."""
        await self.redis.set('bill_dispenser:upper_lvl', upper_lvl)
        await self.redis.set('bill_dispenser:lower_lvl', lower_lvl)


    @redis_error_handler("Количество купюр диспенсера установлено успешно")
    async def set_bill_dispenser_count(self, upper_count, lower_count):
        """
        Изменение количества купюр в диспенсере.
        Прибавляет переданное значение к существующему.
        """
        old_upper_count = int(await self.redis.get('bill_dispenser:upper_count'))
        old_lower_count = int(await self.redis.get('bill_dispenser:lower_count'))
        await self.redis.set('bill_dispenser:upper_count', upper_count + old_upper_count)
        await self.redis.set('bill_dispenser:lower_count', lower_count + old_lower_count)


    @redis_error_handler("Количество купюр в диспенсере обнулено успешно")
    async def bill_dispenser_reset_bill_count(self):
        """Сброс количества купюр в диспенсере."""
        await self.redis.set('bill_dispenser:upper_count', 0)
        await self.redis.set('bill_dispenser:lower_count', 0)


    async def stop_accepting_payment(self):
        """Остановка активного платежа."""
        await self.bill_acceptor.stop_accepting()
        self.is_payment_in_progress = False
        logger.info('Платеж остановлен успешно')
        return {
            'success': True,
            'message': 'Платеж остановлен успешно',
        }

    @redis_error_handler("Тест выдачи сдачи прошел успешно")
    async def test_dispense_change(self):
        self.upper_box_value = int(await self.redis.get('bill_dispenser:upper_lvl'))
        self.lower_box_value = int(await self.redis.get('bill_dispenser:lower_lvl'))
        await self.dispense_change(self.upper_box_value + self.lower_box_value)


    async def init_devices(self):
        """Инициализация устройств."""
        await self.init_coin_acceptor()
        await self.init_bill_acceptor()
        await self.init_bill_dispenser()

        self.register_event_handlers()
        asyncio.create_task(self.event_consumer.start_consuming())

        available_devices = await self.redis.smembers("available_devices_cash")
        if available_devices == self.active_devices:
            logger.info('Платежная система инициализирована успешно')
            return {
                'success': True,
                'message': 'Платежная система инициализирована успешно',
            }
        else:
            logger.error(
                f'Не удалось инициализировать устройтсва: '
                f'{available_devices - self.active_devices}')
            return {
                'success': False,
                'message': f'Не удалось инициализировать устройтсва: '
                           f'{available_devices - self.active_devices}',
            }


    async def init_coin_acceptor(self):
        """Инициализация Smart Hopper."""
        try:
            self.hopper.open(COIN_ACCEPTOR_PORT, PORT_OPTIONS)

            await self.hopper.command('SYNC')
            await self.hopper.command('HOST_PROTOCOL_VERSION', {'version': 6})
            await self.hopper.init_encryption()
            await self.hopper.command('SETUP_REQUEST')

            logger.info('Монетоприемник инициализирован успешно')
            self.active_devices.add("coin_acceptor")
        except Exception as e:
            logger.error(f'Ошибка инициализации монетоприемника: {e}')


    async def init_bill_acceptor(self):
        """Инициализация bill acceptor."""
        try:
            if not await self.bill_acceptor.initialize():
                raise
            await self.bill_acceptor.reset_device()
            logger.info("Купюроприемник инициализирован успешно")
            self.active_devices.add("bill_acceptor")
        except Exception as e:
            logger.error(f"Ошибка инициализации купюроприемника: {e}")


    async def init_bill_dispenser(self):
        """Инициализация bill dispenser."""
        try:
            self.bill_dispenser.connect(BILL_DISPENSER_PORT, 9600)
            self.bill_dispenser.purge()
            logger.info('Bill dispenser инициализирован успешно')
            self.active_devices.add("bill_dispenser")
        except LcdmException as e:
            logger.error(f'Ошибка соединения при инициализации Bill dispenser: {e}')


    def register_event_handlers(self):
        """Регистрация обработчиков для событий приема монет и купюр."""
        self.event_consumer.register_handler(EventType.BILL_ACCEPTED, self.handle_bill_accepted)
        self.event_consumer.register_handler(EventType.COIN_CREDIT, self.on_coin_credit)


    async def handle_bill_accepted(self, event):
        """Обработчик принятия купюры."""
        bill_value = event['value']
        self.collected_amount += bill_value
        await self.redis.set('collected_amount', self.collected_amount)

        logger.info(f"Принята купюра: {bill_value} рублей. Всего принято: {self.collected_amount} рублей")
        await send_to_ws(
            event='acceptedBill',
            detail=f"Принята купюра: {bill_value} рублей. Всего принято: {self.collected_amount} рублей",
            data={'bill_value': bill_value, 'collected_amount': self.collected_amount},
        )

        if self.target_amount != 0 and self.collected_amount >= self.target_amount:
            await self.complete_payment()


    async def on_coin_credit(self, event):
        """Обработчик принятия монеты."""
        try:
            coin_data = event.get('info').get("value")[0]
            num = coin_data.get("value")
            amount_map = {1375731712: 1, 1375731713: 5, 1375731715: 10}

            if len(event.get('info').get("value")) == 200 and amount_map.get(num) == 1:
                amount = 2
            else:
                amount = amount_map.get(num, None)

            if amount is None:
                logger.error(f"Ошибка, неизвестная монета: {num}")
                return

            self.collected_amount += amount
            await self.redis.set('collected_amount', self.collected_amount)

            logger.info(f"Получена монета: {amount} рублей. Всего: {self.collected_amount} рублей")

            # Check if we reached or exceeded the target
            if (self.collected_amount >= self.target_amount) and (self.target_amount > 0):
                await self.complete_payment()

        except Exception as e:
            logger.error(f'Ошибка при получении монеты: {e}')


    async def start_accepting_payment(self, amount):
        """Начало платежа."""
        upper_box_count = int(await self.redis.get('bill_dispenser:upper_count'))
        lower_box_count = int(await self.redis.get('bill_dispenser:lower_count'))
        bill_count = await self.redis.set('bill_count')
        max_bill_count = await self.redis.set('max_bill_count')

        if self.is_payment_in_progress:
            logger.error('Платеж уже запущен')
            return {
                'success': False,
                'message': 'Платеж уже запущен',
            }
        elif upper_box_count < MIN_BOX_COUNT or lower_box_count < MIN_BOX_COUNT:
            logger.error(f'В устройстве bill_dispenser не достаточно купюр.'
                         f'Верхний бокс: {upper_box_count}. Нижний бокс: {lower_box_count}.')
            return {
                'success': False,
                'message': 'В устройстве bill_dispenser не достаточно купюр.',
            }
        elif bill_count >= max_bill_count:
            logger.error('Устройство bill acceptor переполнено')
            return {
                'success': False,
                'message': 'Устройство bill acceptor переполнено',
            }

        logger.info(f"Начат прием на сумму {amount} рублей")

        self.target_amount = amount
        self.collected_amount = 0
        self.is_payment_in_progress = True

        await self.redis.set('target_amount', amount)
        await self.redis.set('collected_amount', self.collected_amount)

        devices_started = []

        if "coin_acceptor" in self.active_devices:
            await self.hopper.enable()
            devices_started.append("coin acceptor")

        if "bill_acceptor" in self.active_devices and self.bill_acceptor:
            await self.bill_acceptor.start_accepting()
            devices_started.append("bill acceptor")

        if devices_started:
            self.is_payment_in_progress = True
            return {
                'success': True,
                'message': f"Начат прием на сумму {amount} рублей",
            }
        else:
            self.is_payment_in_progress = False
            logger.error('Нет активных девайсов')
            return {
                'success': False,
                'message': 'Нет активных девайсов',
            }


    async def complete_payment(self):
        """Успешное завершение платежа."""
        if "coin_acceptor" in self.active_devices:
            await self.hopper.disable()

        if "bill_acceptor" in self.active_devices and self.bill_acceptor:
            await self.bill_acceptor.stop_accepting()

        change = max(0, self.collected_amount - self.target_amount)
        self.is_payment_in_progress = False
        self.target_amount = 0

        logger.info(f"Платеж завершен успешно. Принято "
                    f"{self.collected_amount} рублей. Сдача: {change} рублей")
        await send_to_ws(
            event='successPayment',
            detail='Платеж завершен успешно',
            data={'collected_amount': self.collected_amount, 'change': change},
        )

        if change > 0:
            await self.dispense_change(change)

        # сброс счетчиков redis
        await self.redis.set('collected_amount', 0)
        await self.redis.set('target_amount', 0)


    async def dispense_change(self, amount):
        """Выдача сдачи."""
        dispensed_amount = 0

        # Сначала пробуем выдать купюры
        if "bill_dispenser" in self.active_devices and amount >= self.lower_box_value:
            try:
                # Определяем какой номинал больше
                higher_box_value = max(self.upper_box_value, self.lower_box_value)
                lower_box_value = min(self.upper_box_value, self.lower_box_value)

                # Сначала используем больший номинал, затем меньший
                higher_bills = int(amount // higher_box_value)
                lower_bills = int((amount % higher_box_value) // lower_box_value)

                if higher_bills > 0 or lower_bills > 0:
                    # В зависимости от того, какой номинал был больше, передаем параметры в правильном порядке
                    if self.upper_box_value > self.lower_box_value:
                        result = self.bill_dispenser.upperLowerDispense(higher_bills, lower_bills)
                    else:
                        result = self.bill_dispenser.upperLowerDispense(lower_bills, higher_bills)

                    upper_exit, lower_exit, upper_rejected, lower_rejected, upper_check, lower_check = result

                    dispensed_amount = (upper_exit * self.upper_box_value + lower_exit * self.lower_box_value)
                    amount -= dispensed_amount

                    upper_count = await self.redis.get('bill_dispenser:upper_count')
                    lower_count = await self.redis.get('bill_dispenser:lower_count')
                    new_upper = upper_count - upper_exit
                    new_lower = lower_count - lower_exit
                    await self.redis.set('bill_dispenser:upper_count', new_upper)
                    await self.redis.set('bill_dispenser:lower_count', new_lower)

            except Exception as e:
                logger.error(f'Ошибка при выдаче купюр: {e}')
                return {
                    'success': False,
                    'message': f'Ошибка при выдаче купюр: {e}',
                }

        if "coin_acceptor" in self.active_devices:
            try:
                await self.hopper.enable()
                coins_to_dispense = int(amount * 100)
                result = await self.hopper.command('PAYOUT_AMOUNT', {
                    'amount': coins_to_dispense,
                    'country_code': 'RUB',
                    'test': False
                })

                if result.get("success"):
                    dispensed_amount += amount
                    amount = 0
                else:
                    error_msg = f"Coin payout failed: {result.get('error', 'Unknown error')}"
                    logger.error(error_msg)

            except Exception as e:
                error_msg = f"Ошибка при выдаче монет: {str(e)}"
                logger.error(error_msg)
            finally:
                await self.hopper.disable()

        if amount > 0:
            logger.info(f"Остаток не выданной сдачи: {amount} RUB")

        if dispensed_amount > 0:
            remainder = self.collected_amount - dispensed_amount
            logger.info(f"Выдано сдачи: {dispensed_amount} RUB, невыданный остаток: {remainder}")
            return {
                'success': True,
                'message': 'Сдача выдана успешно',
            }
        else:
            logger.info("Сдача не выдана")
            return {
                'success': False,
                'message': 'Сдача не выдана',
            }


    async def shutdown(self):
        """Завершение работы с устройствами."""
        try:
            if "coin_acceptor" in self.active_devices:
                await self.hopper.disable()
                await self.hopper.close()

            if "bill_acceptor" in self.active_devices and self.bill_acceptor:
                await self.bill_acceptor.stop_accepting()

            # Stop event consumer
            await self.event_consumer.stop_consuming()

            logger.info("Платежная система выключена успешно")
        except Exception as e:
            logger.error(f"Ошибка выключения платежной системы: {e}")
