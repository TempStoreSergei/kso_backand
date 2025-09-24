import asyncio
from typing import AsyncIterator

import aioserial
import httpx
from redis.asyncio import Redis

from funcs import get_sdn_hosts, item_without_basket_process, default_item_process, \
    find_serial_device_by_name, only_baskets_process
from config import REDIS_HOST, REDIS_PORT
from loggers import logger


async def read_barcode(device_path: str) -> AsyncIterator[str]:
    """
    Читает штрих-коды из COM-порта (USB Virtual COM).
    """
    while True:
        try:
            serial_port = aioserial.AioSerial(port=device_path, baudrate=9600)
            logger.info(f"Успешно подключено и начато прослушивание порта {device_path}")

            buffer = bytearray()

            while True:
                byte = await serial_port.read_async()
                if byte in (b'\r', b'\n'):
                    barcode = buffer.decode('utf-8', errors='ignore').strip()
                    buffer.clear()
                    if barcode:
                        yield barcode
                else:
                    buffer += byte

        except aioserial.SerialException as e:
            logger.error(f"Ошибка порта {device_path}: {e}. Повтор через 5 сек...")
        except Exception as e:
            logger.error(f"Критическая ошибка: {e}")
        await asyncio.sleep(5) # Пауза перед попыткой переподключения


async def monitor_barcodes(serial_device_path: str, redis: Redis) -> None:
    """Мониторит штрих-коды и обрабатывает их."""
    logger.info("Мониторинг штрих-кодов запущен")
    sdn_hosts = await get_sdn_hosts()
    try:
        async for barcode in read_barcode(serial_device_path):
            try:
                logger.info(f'Баракод: {repr(barcode)}')
                async with httpx.AsyncClient() as client:
                    item_without_basket = await redis.get("item_without_basket")
                    pay_in_progress = await redis.get("pay_in_progress")
                    only_baskets = await redis.get('only_baskets')
                    logger.debug(f'!!!!!!!!!!{pay_in_progress}')
                    if pay_in_progress:
                        logger.info(
                            "Корзина уже находится в процессе оплаты, нельзя сканировать товары."
                        )
                        await asyncio.sleep(1)
                    elif only_baskets:
                        await only_baskets_process(barcode, client)
                    elif item_without_basket:
                        await item_without_basket_process(barcode, redis, client, sdn_hosts)
                    else:
                        await default_item_process(barcode, redis, client, sdn_hosts)
                    continue

            except Exception as e:
                logger.error(f"Критическая ошибка в monitor_barcodes: {e}")
    except asyncio.CancelledError:
        logger.error("Мониторинг штрих-кодов остановлен")


async def main():
    """Основная функция приложения."""
    logger.info("Поиск COM-порта сканера штрих-кодов...")
    redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    serial_dev = find_serial_device_by_name()
    if not serial_dev:
        logger.error("Сканер не найден. Проверьте подключение и режим работы (USB Virtual COM).")
        return

    logger.info(f"Найдено устройство: {serial_dev}")

    task = asyncio.create_task(monitor_barcodes(serial_dev, redis=redis))

    try:
        await task
    except asyncio.CancelledError:
        logger.info("Задача была отменена")
    except KeyboardInterrupt:
        logger.info("\nПолучен сигнал прерывания. Останавливаю...")
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            logger.info("Задача корректно отменена")
        logger.info("Программа завершена.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Программа завершена пользователем")
