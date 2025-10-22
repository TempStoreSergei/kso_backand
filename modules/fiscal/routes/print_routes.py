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
        description="Напечатать строку текста с форматированием",
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
        description="Промотать чековую ленту на N пустых строк",
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
        description="Напечатать одномерный или двумерный штрихкод (QR, EAN-13, PDF417, и др.)",
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
        description="Напечатать картинку из файла (BMP или PNG без прозрачности)",
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
        description="Напечатать картинку из памяти ККТ по номеру",
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
        description="Открыть нефискальный документ для печати",
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
        description="Закрыть нефискальный документ и отрезать чек",
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
        description="Отрезать чековую ленту",
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
        description="Подать сигнал на открытие денежного ящика",
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
        description="Подать звуковой сигнал через динамик ККТ",
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
        description="Сыграть мелодию 'Enemy' из сериала Arcane",
        responses={
            status.HTTP_200_OK: {
                "description": "Мелодия успешно воспроизведена",
            },
        },
    ),
]
