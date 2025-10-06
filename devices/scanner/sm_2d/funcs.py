import base64

import httpx
from evdev import InputDevice, list_devices

from config import API_URL
from loggers import logger


def find_scanner_device():
    """Поиск USB HID сканера среди устройств"""
    devices = [InputDevice(path) for path in list_devices()]

    for device in devices:
        if device.name == 'SM SM-2D PRODUCT HID KBW':
            logger.info(f"✓ Найден сканер: {device.name}")
            return device

    logger.info("✗ Сканер не найден!")
    return None


async def send_to_api(scanned_code: str):
    """Отправка отсканированного кода на API"""
    encoded = base64.b64encode(scanned_code.encode("utf-8")).decode("utf-8")

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.post(API_URL, json={"scanned_code": encoded})
            response.raise_for_status()
            logger.info(f"✓ Отправлено на сервер")
        except httpx.HTTPStatusError as e:
            logger.error(f"✗ Ошибка HTTP {e.response.status_code}: {e.response.text}")
        except httpx.RequestError as e:
            logger.error(f"✗ Ошибка соединения: {e}")
        except Exception as e:
            logger.error(f"✗ Ошибка: {e}")
