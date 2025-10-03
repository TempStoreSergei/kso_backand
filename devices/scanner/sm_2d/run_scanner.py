import asyncio

import evdev
from evdev import InputDevice, categorize, ecodes

from config import SCAN_CODES, SHIFT_ENCODES
from funcs import find_scanner_device, send_to_api
from loggers import logger


async def process_barcode(scanned_code: str):
    """Обработка отсканированного штрихкода"""
    logger.info(f"Отсканировано: {scanned_code}")

    # Проверяем наличие символа GS (char 29)
    if chr(29) in scanned_code:
        gs_pos = scanned_code.index(chr(29))
        logger.debug(f"✓ Обнаружен символ GS (char 29) в позиции {gs_pos}")

    # Отправляем на API
    await send_to_api(scanned_code)


async def read_scanner():
    """Основная функция чтения данных со сканера"""
    try:
        device = find_scanner_device()

        if not device:
            return

        logger.info(f"\nГотов к сканированию. Для выхода нажмите Ctrl+C\n")

        # Захват устройства для эксклюзивного доступа
        device.grab()

        barcode = []
        shift_pressed = False

        # Читаем события в асинхронном режиме
        async for event in device.async_read_loop():
            if event.type == ecodes.EV_KEY:
                data = categorize(event)

                # Обрабатываем только нажатия (не отпускания)
                if data.keystate == 1:  # key down
                    scancode = data.scancode

                    # Обработка модификаторов
                    if scancode == 42 or scancode == 54:  # SHIFT
                        shift_pressed = True
                        continue
                    elif scancode == 66:  # GS (Group Separator, char 29)
                        barcode.append(chr(29))
                        continue

                    # Обработка Enter - завершение ввода штрихкода
                    if scancode == 28:  # ENTER
                        if barcode:
                            scanned_code = ''.join(barcode)
                            await process_barcode(scanned_code)
                            barcode = []
                        shift_pressed = False
                        continue

                    # Получаем символ
                    if shift_pressed and scancode in SHIFT_ENCODES:
                        char = SHIFT_ENCODES[scancode]
                    elif scancode in SCAN_CODES:
                        char = SCAN_CODES[scancode]
                    else:
                        char = None

                    # Добавляем символ в буфер
                    if char and char not in ['LSHIFT', 'RSHIFT', 'CTRL', 'ALT', 'RALT', 'ESC',
                                             'TAB', 'BKSP']:
                        barcode.append(char)

                elif data.keystate == 0:  # key up
                    scancode = data.scancode
                    if scancode == 42 or scancode == 54:
                        shift_pressed = False

    except KeyboardInterrupt:
        logger.info("\n\n✓ Остановка чтения...")
    except Exception as e:
        logger.error(f"✗ Ошибка: {e}")
    finally:
        device.ungrab()


if __name__ == "__main__":
    try:
        asyncio.run(read_scanner())
    except KeyboardInterrupt:
        logger.info("Программа завершена пользователем")
