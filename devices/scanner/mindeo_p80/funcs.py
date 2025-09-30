import os

import serial.tools.list_ports

from loggers import logger


def find_serial_device(vendor_id: int, product_id: int) -> str | None:
    """
    Ищет COM-порт сканера по VID/PID.
    Возвращает строку с путем, например '/dev/ttyACM0', или None, если не найдено.
    VID 0x1EAB - стандартный для Mindeo. PID может отличаться.
    """
    ports = serial.tools.list_ports.comports()
    logger.debug(f"Поиск среди доступных портов: {[p.device for p in ports]}")

    # 1. Приоритетный поиск по VID (и PID, если указан)
    for port in ports:
        if port.vid == vendor_id and (product_id is None or port.pid == product_id):
            logger.info(f"Найден сканер Mindeo по VID/PID: {port.device} ({port.description})")
            return port.device

    # 2. Резервный поиск по описанию, если по VID/PID не нашлось
    for port in ports:
        desc = port.description.lower()
        if "scanner" in desc or "mindeo" in desc or "barcode" in desc:
            logger.info(f"Найдено COM-устройство по описанию: {port.device} ({port.description})")
            return port.device

    return None


def find_serial_device_by_name(
    name_substring: str = "usb-Linux_3.10.14_with_dwc2-gadget_GadGet_Serial_v2.4-if00"
) -> str | None:
    """
    Ищет COM-порт по части имени в /dev/serial/by-id/.
    Возвращает путь к устройству (например, '/dev/serial/by-id/...') или None, если не найдено.
    """
    search_path = "/dev/serial/by-id/"
    try:
        for entry in os.listdir(search_path):
            if name_substring in entry:
                full_path = os.path.realpath(os.path.join(search_path, entry))
                logger.info(f"Найден порт по имени: {entry} -> {full_path}")
                return full_path
    except FileNotFoundError:
        logger.warning(f"Каталог {search_path} не найден — вероятно, нет подключенных USB-UART устройств.")
    return None
