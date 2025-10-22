from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.printer.beep_dto import BeepRequest
from modules.fiscal.DTO.printer.feed_line_dto import PrintFeedRequest
from modules.fiscal.DTO.printer.print_barcode_dto import PrintBarcodeRequest
from modules.fiscal.DTO.printer.print_picture_dto import PrintPictureRequest, \
    PrintPictureByNumberRequest
from modules.fiscal.DTO.printer.print_text_dto import PrintTextRequest


async def print_text(
    request: PrintTextRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Напечатать строку текста с форматированием.

    **Параметры:**
    - **text**: Строка для печати
    - **alignment**: Выравнивание (0=влево, 1=центр, 2=вправо)
    - **wrap**: Перенос строк (0=нет, 1=по словам, 2=по символам)
    - **font**: Номер шрифта (опционально, зависит от модели ККТ)
    - **double_width**: Двойная ширина шрифта (опционально)
    - **double_height**: Двойная высота шрифта (опционально)
    - **linespacing**: Межстрочный интервал (опционально)
    - **brightness**: Яркость печати (опционально)
    - **defer**: Отложенная печать (0=нет, 1=перед чеком, 2=после чека, 3=рядом с ШК)

    **Примеры:**
    ```json
    // Простой текст
    {"text": "Привет, мир!"}

    // Текст по центру с двойной шириной
    {"text": "ВНИМАНИЕ!", "alignment": 1, "double_width": true}

    // Текст с переносом по словам
    {"text": "Очень длинная строка которая не поместится", "wrap": 1}
    ```
    """
    command = {
        "device_id": device_id,
        "command": "print_text",
        "kwargs": request.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def feed_line(
    request: PrintFeedRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Промотать чековую ленту на N пустых строк.

    **Внимание:** Не рекомендуется печатать вне открытых документов!
    """
    command = {
        "device_id": device_id,
        "command": "print_feed",
        "kwargs": request.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def print_barcode(
    request: PrintBarcodeRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Напечатать штрихкод.

    **Типы штрихкодов:**

    *Одномерные:*
    - 0 = EAN-8
    - 1 = EAN-13
    - 2 = UPC-A
    - 3 = UPC-E
    - 4 = Code 39
    - 5 = Code 93
    - 6 = Code 128
    - 7 = Codabar
    - 8 = ITF (Interleaved 2of5)
    - 9 = ITF-14
    - 10 = GS1-128 (EAN-128)
    - 11 = Code 39 Extended

    *Двумерные:*
    - 17 = QR-код (по умолчанию)
    - 18 = PDF417
    - 19 = AZTEC

    **Примеры:**
    ```json
    // Простой QR-код
    {"barcode": "https://example.com", "barcode_type": 17}

    // EAN-13 с увеличением
    {"barcode": "4607123456789", "barcode_type": 1, "scale": 3}

    // QR по центру с коррекцией
    {"barcode": "Большой текст", "barcode_type": 17, "alignment": 1, "correction": 3, "scale": 4}
    ```

    **GS1-128:** AI заключаются в квадратные скобки:
    ```json
    {"barcode": "[01]98898765432106[3202]012345[15]991231", "barcode_type": 10}
    ```
    """
    command = {
        "device_id": device_id,
        "command": "print_barcode",
        "kwargs": request.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def print_picture(
    request: PrintPictureRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Напечатать картинку из файла.

    **Поддерживаемые форматы:** BMP и PNG без прозрачности

    **Примеры:**
    ```json
    // Печать логотипа по центру
    {"filename": "/path/to/logo.png", "alignment": 1, "scale_percent": 100}

    // Уменьшенная картинка
    {"filename": "C:\\\\images\\\\receipt_header.bmp", "scale_percent": 50}
    ```

    **Внимание:** Не рекомендуется печатать вне открытых документов!
    """
    command = {
        "device_id": device_id,
        "command": "print_picture",
        "kwargs": request.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def print_picture_by_number(
    request: PrintPictureByNumberRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Напечатать картинку из памяти ККТ.

    Картинки должны быть предварительно загружены в память ККТ.
    Нумерация картинок начинается с 0.

    **Примеры:**
    ```json
    // Печать логотипа (картинка №0)
    {"picture_number": 0, "alignment": 1}

    // Картинка перед чеком
    {"picture_number": 1, "defer": 1}
    ```

    **Внимание:** Не рекомендуется печатать вне открытых документов!
    """
    command = {
        "device_id": device_id,
        "command": "print_picture_by_number",
        "kwargs": request.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def open_nonfiscal_document(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Открыть нефискальный документ.

    **Важно:** Нефискальный документ - это чек, который не передается в ОФД.
    Используется для печати служебной информации, логотипов, объявлений и т.д.

    **Обязательно закрывайте документ** после печати с помощью `/document/close`!

    **Порядок работы:**
    1. Открыть документ (`/document/open`)
    2. Печатать текст, штрихкоды, картинки (`/text`, `/barcode`, `/picture`)
    3. Закрыть документ (`/document/close`)
    """
    command = {
        "device_id": device_id,
        "command": "open_nonfiscal_document"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def close_nonfiscal_document(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Закрыть нефискальный документ.

    Завершает печать нефискального документа и отрезает чек.
    """
    command = {
        "device_id": device_id,
        "command": "close_nonfiscal_document"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def cut_paper(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Отрезать чековую ленту.

    Используется для отрезания чека после завершения печати.
    """
    command = {
        "device_id": device_id,
        "command": "cut_paper"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def open_cash_drawer(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Открыть денежный ящик.

    Подает сигнал на открытие денежного ящика, подключенного к ККТ.
    """
    command = {
        "device_id": device_id,
        "command": "open_cash_drawer"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def beep(
    request: BeepRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Подать звуковой сигнал через динамик ККТ.

    Параметры:
    - **frequency**: Частота звука в Гц (100-10000). По умолчанию 2000 Гц
    - **duration**: Длительность звука в мс (10-5000). По умолчанию 100 мс

    Примеры частот:
    - 262 Гц - До (C4)
    - 294 Гц - Ре (D4)
    - 330 Гц - Ми (E4)
    - 349 Гц - Фа (F4)
    - 392 Гц - Соль (G4)
    - 440 Гц - Ля (A4)
    - 494 Гц - Си (B4)
    - 523 Гц - До (C5)
    """
    command = {
        "device_id": device_id,
        "command": "beep",
        "kwargs": request.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def play_arcane_melody(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Сыграть мелодию "Enemy" из сериала Arcane через динамик ККТ!

    🎵 Everybody wants to be my enemy... 🎵

    Воспроизводит упрощённую версию главной темы из Arcane (Imagine Dragons feat. JID).
    Примерная длительность: ~15 секунд.

    **Внимание**: Во время воспроизведения мелодии ККТ будет занята и не сможет
    выполнять другие операции.
    """
    command = {
        "device_id": device_id,
        "command": "play_arcane_melody"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
