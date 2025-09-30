import asyncio
import base64
from typing import AsyncIterator

import aioserial
import httpx

from funcs import find_serial_device, find_serial_device_by_name
from loggers import logger
from config import API_URL


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
                await asyncio.sleep(5)
                continue 

        except Exception as e:
            logger.error(f"Критическая ошибка в read_barcode: {e}. Повторная попытка через 5 секунд...")
        
        await asyncio.sleep(5) # Пауза перед попыткой переподключения

async def monitor_barcodes(serial_device_path: str) -> None:
    """Мониторит штрих-коды и обрабатывает их."""
    logger.info("Мониторинг штрих-кодов запущен")
    try:
        async for barcode in read_barcode(serial_device_path):

            logger.info(f'Баракод: {repr(barcode)}')
            encoded = base64.b64encode(barcode.encode("utf-8")).decode("utf-8")

            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(API_URL, json={"scanned_code": encoded})
                    response.raise_for_status()
                except httpx.HTTPStatusError as e:
                    # Сервер ответил, но код ответа (4xx/5xx)
                    logger.error(f"Ошибка HTTP {e.response.status_code}: {e.response.text}")
                except httpx.RequestError as e:
                    # Проблема с соединением (нет сети, таймаут и т.д.)
                    logger.error(f"Ошибка при запросе: {e}")
            
    except asyncio.CancelledError:
        logger.error("Мониторинг штрих-кодов остановлен")


async def main():
    """Основная функция приложения."""
    logger.info("Поиск COM-порта сканера штрих-кодов...")
    
    scaner = find_serial_device(vendor_id=0x27dd, product_id=0xe081)
    manual_scaner = find_serial_device_by_name()
    if not any([scaner, manual_scaner]):
        logger.error("Сканеры не найдены. Проверьте подключение и режим работы (USB Virtual COM).")
        return
    if not scaner:
        logger.warning("Встроенный сканер не найден.")
    else:
        logger.info(f"Найден встроенный сканер: {scaner}")

    if not manual_scaner:
        logger.warning("Ручной сканер не найден.")
    else:
        logger.info(f"Найден ручной сканер: {manual_scaner}")

    tasks = []
    if scaner:
        tasks.append(asyncio.create_task(monitor_barcodes(scaner)))
    if manual_scaner:
        tasks.append(asyncio.create_task(monitor_barcodes(manual_scaner)))

    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        logger.info("Задачи были отменены")
    except KeyboardInterrupt:
        logger.info("\nПолучен сигнал прерывания. Останавливаю...")
        for task in tasks:
            task.cancel()
        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            logger.info("Задачи корректно отменены")
        logger.info("Программа завершена.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Программа завершена пользователем")
