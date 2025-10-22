from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.endpoints.print_endpoints import *


PRINT_ROUTES = [
    RouteDTO(
        path="/text",
        endpoint=print_text,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Печать текста",
        description="Напечатать строку текста с форматированием.\n\n**Параметры:**\n- **text**: Строка для печати\n- **alignment**: Выравнивание (0=влево, 1=центр, 2=вправо)\n- **wrap**: Перенос строк (0=нет, 1=по словам, 2=по символам)\n- **font**: Номер шрифта (опционально, зависит от модели ККТ)\n- **double_width**: Двойная ширина шрифта (опционально)\n- **double_height**: Двойная высота шрифта (опционально)\n- **linespacing**: Межстрочный интервал (опционально)\n- **brightness**: Яркость печати (опционально)\n- **defer**: Отложенная печать (0=нет, 1=перед чеком, 2=после чека, 3=рядом с ШК)\n\n**Примеры:**\n```json\n// Простой текст\n{\"text\": \"Привет, мир!\"}\n\n// Текст по центру с двойной шириной\n{\"text\": \"ВНИМАНИЕ!\", \"alignment\": 1, \"double_width\": true}\n\n// Текст с переносом по словам\n{\"text\": \"Очень длинная строка которая не поместится\", \"wrap\": 1}\n```",
        responses={
            status.HTTP_200_OK: {
                "description": "Текст успешно напечатан",
            },
        },
    ),
    RouteDTO(
        path="/feed",
        endpoint=feed_line,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Промотка ленты",
        description="Промотать чековую ленту на N пустых строк.\n\n**Внимание:** Не рекомендуется печатать вне открытых документов!",
        responses={
            status.HTTP_200_OK: {
                "description": "Лента успешно промотана",
            },
        },
    ),
    RouteDTO(
        path="/barcode",
        endpoint=print_barcode,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Печать штрихкода",
        description="Напечатать штрихкод.\n\n**Типы штрихкодов:**\n\n*Одномерные:*\n- 0 = EAN-8\n- 1 = EAN-13\n- 2 = UPC-A\n- 3 = UPC-E\n- 4 = Code 39\n- 5 = Code 93\n- 6 = Code 128\n- 7 = Codabar\n- 8 = ITF (Interleaved 2of5)\n- 9 = ITF-14\n- 10 = GS1-128 (EAN-128)\n- 11 = Code 39 Extended\n\n*Двумерные:*\n- 17 = QR-код (по умолчанию)\n- 18 = PDF417\n- 19 = AZTEC\n\n**Примеры:**\n```json\n// Простой QR-код\n{\"barcode\": \"https://example.com\", \"barcode_type\": 17}\n\n// EAN-13 с увеличением\n{\"barcode\": \"4607123456789\", \"barcode_type\": 1, \"scale\": 3}\n\n// QR по центру с коррекцией\n{\"barcode\": \"Большой текст\", \"barcode_type\": 17, \"alignment\": 1, \"correction\": 3, \"scale\": 4}\n```\n\n**GS1-128:** AI заключаются в квадратные скобки:\n```json\n{\"barcode\": \"[01]98898765432106[3202]012345[15]991231\", \"barcode_type\": 10}\n```",
        responses={
            status.HTTP_200_OK: {
                "description": "Штрихкод успешно напечатан",
            },
        },
    ),
    RouteDTO(
        path="/picture",
        endpoint=print_picture,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Печать картинки из файла",
        description="Напечатать картинку из файла.\n\n**Поддерживаемые форматы:** BMP и PNG без прозрачности\n\n**Примеры:**\n```json\n// Печать логотипа по центру\n{\"filename\": \"/path/to/logo.png\", \"alignment\": 1, \"scale_percent\": 100}\n\n// Уменьшенная картинка\n{\"filename\": \"C:\\\\\\\\images\\\\\\\\receipt_header.bmp\", \"scale_percent\": 50}\n```\n\n**Внимание:** Не рекомендуется печатать вне открытых документов!",
        responses={
            status.HTTP_200_OK: {
                "description": "Картинка успешно напечатана",
            },
        },
    ),
    RouteDTO(
        path="/picture-by-number",
        endpoint=print_picture_by_number,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Печать картинки из памяти",
        description="Напечатать картинку из памяти ККТ.\n\nКартинки должны быть предварительно загружены в память ККТ.\nНумерация картинок начинается с 0.\n\n**Примеры:**\n```json\n// Печать логотипа (картинка №0)\n{\"picture_number\": 0, \"alignment\": 1}\n\n// Картинка перед чеком\n{\"picture_number\": 1, \"defer\": 1}\n```\n\n**Внимание:** Не рекомендуется печатать вне открытых документов!",
        responses={
            status.HTTP_200_OK: {
                "description": "Картинка успешно напечатана",
            },
        },
    ),
    RouteDTO(
        path="/document/open",
        endpoint=open_nonfiscal_document,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Открыть нефискальный документ",
        description="Открыть нефискальный документ.\n\n**Важно:** Нефискальный документ - это чек, который не передается в ОФД.\nИспользуется для печати служебной информации, логотипов, объявлений и т.д.\n\n**Обязательно закрывайте документ** после печати с помощью `/document/close`!\n\n**Порядок работы:**\n1. Открыть документ (`/document/open`)\n2. Печатать текст, штрихкоды, картинки (`/text`, `/barcode`, `/picture`)\n3. Закрыть документ (`/document/close`)",
        responses={
            status.HTTP_200_OK: {
                "description": "Нефискальный документ открыт",
            },
        },
    ),
    RouteDTO(
        path="/document/close",
        endpoint=close_nonfiscal_document,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Закрыть нефискальный документ",
        description="Закрыть нефискальный документ.\n\nЗавершает печать нефискального документа и отрезает чек.",
        responses={
            status.HTTP_200_OK: {
                "description": "Нефискальный документ закрыт",
            },
        },
    ),
    RouteDTO(
        path="/cut",
        endpoint=cut_paper,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Отрезать чек",
        description="Отрезать чековую ленту.\n\nИспользуется для отрезания чека после завершения печати.",
        responses={
            status.HTTP_200_OK: {
                "description": "Лента отрезана",
            },
        },
    ),
    RouteDTO(
        path="/open-drawer",
        endpoint=open_cash_drawer,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Открыть денежный ящик",
        description="Открыть денежный ящик.\n\nПодает сигнал на открытие денежного ящика, подключенного к ККТ.",
        responses={
            status.HTTP_200_OK: {
                "description": "Денежный ящик открыт",
            },
        },
    ),
    RouteDTO(
        path="/beep",
        endpoint=beep,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Звуковой сигнал",
        description="Подать звуковой сигнал через динамик ККТ.\n\nПараметры:\n- **frequency**: Частота звука в Гц (100-10000). По умолчанию 2000 Гц\n- **duration**: Длительность звука в мс (10-5000). По умолчанию 100 мс\n\nПримеры частот:\n- 262 Гц - До (C4)\n- 294 Гц - Ре (D4)\n- 330 Гц - Ми (E4)\n- 349 Гц - Фа (F4)\n- 392 Гц - Соль (G4)\n- 440 Гц - Ля (A4)\n- 494 Гц - Си (B4)\n- 523 Гц - До (C5)",
        responses={
            status.HTTP_200_OK: {
                "description": "Звуковой сигнал воспроизведён",
            },
        },
    ),
    RouteDTO(
        path="/play-arcane",
        endpoint=play_arcane_melody,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Мелодия Arcane",
        description="Сыграть мелодию \"Enemy\" из сериала Arcane через динамик ККТ!\n\nВоспроизводит упрощённую версию главной темы из Arcane (Imagine Dragons feat. JID).\nПримерная длительность: ~15 секунд.\n\n**Внимание**: Во время воспроизведения мелодии ККТ будет занята и не сможет\nвыполнять другие операции.",
        responses={
            status.HTTP_200_OK: {
                "description": "Мелодия успешно воспроизведена",
            },
        },
    ),
]
