import asyncio
from typing import AsyncIterator

import aioserial
import httpx
from redis.asyncio import Redis

from funcs import find_serial_device, get_sdn_hosts, item_without_basket_process, \
    default_item_process, find_serial_device_by_name, only_baskets_process, \
    del_item_fire_mark_process
from config import REDIS_HOST, REDIS_PORT
from loggers import logger


async def read_barcode(device_path: str) -> AsyncIterator[str]:
    """
    Читает штрих-коды из COM-порта (USB Virtual COM).
    Сканер должен быть настроен на отправку суффикса CR (Carriage Return) или CR+LF.
    """
    while True: # Внешний цикл для попыток переподключения
        try:
            serial_port = aioserial.AioSerial(port=device_path, baudrate=9600)
            logger.info(f"Успешно подключено и начато прослушивание порта {device_path}")
            
            while True: # Внутренний цикл чтения данных
                raw_data: bytes = await serial_port.readline_async()
                
                # Декодируем байты в строку и убираем символы \r и \n в конце
                barcode = raw_data.decode('utf-8', errors='ignore').strip()
                
                if barcode:
                    yield barcode

        except aioserial.SerialException as e:
            logger.error(f"Ошибка порта {device_path}: {e}. Повторная попытка через 5 секунд...")
            # Если сканер отключили, порт пропадет
            if "No such file or directory" in str(e):
                logger.error("Сканер был отключен. Ожидание нового подключения...")
                # Не нужно возвращаться в `main`, можно просто подождать здесь.
                await asyncio.sleep(5)
                # Выходим из внутреннего цикла, чтобы внешний цикл попробовал найти устройство заново (если main переписан)
                # В текущей реализации main, лучше просто ждать.
                continue 

        except Exception as e:
            logger.error(f"Критическая ошибка в read_barcode: {e}. Повторная попытка через 5 секунд...")
        
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
                    del_item_fire_mark = await redis.get('del_item_fire_mark')
                    if pay_in_progress:
                        logger.info(
                            "Корзина уже находится в процессе оплаты, нельзя сканировать товары."
                        )
                        await asyncio.sleep(1)
                    elif item_without_basket:
                        await item_without_basket_process(barcode, redis, client, sdn_hosts)
                    elif only_baskets:
                        await only_baskets_process(barcode, redis, client)
                    elif del_item_fire_mark:
                        await del_item_fire_mark_process(barcode, redis, client, del_item_fire_mark)
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
    
    scaner = find_serial_device(vendor_id=0x27dd, product_id=0xe081)
    manual_scaner = find_serial_device_by_name()
    if not all([scaner, manual_scaner]):
        logger.error("Сканер не найден. Проверьте подключение и режим работы (USB Virtual COM).")
        return
    elif not scaner:
        logger.error('Встроенный сканер не найден.')
    elif not manual_scaner:
        logger.error('Ручной сканер не найден')

    logger.info(f"Найдено встроенный сканер: {scaner}")
    logger.info(f"Найдено ручной сканер: {manual_scaner}")

    task_scaner = asyncio.create_task(monitor_barcodes(scaner, redis=redis))
    task_manual_scaner = asyncio.create_task(monitor_barcodes(manual_scaner, redis=redis))

    try:
        await asyncio.gather(task_scaner, task_manual_scaner)
    except asyncio.CancelledError:
        logger.info("Задачи были отменены")
    except KeyboardInterrupt:
        logger.info("\nПолучен сигнал прерывания. Останавливаю...")
        # Отменяем обе задачи
        task_scaner.cancel()
        task_manual_scaner.cancel()
        try:
            await asyncio.gather(task_scaner, task_manual_scaner)
        except asyncio.CancelledError:
            logger.info("Задачи корректно отменены")
        logger.info("Программа завершена.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Программа завершена пользователем")
