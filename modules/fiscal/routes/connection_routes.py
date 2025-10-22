from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.endpoints.connection_endpoints import *


CONNECTION_ROUTES = [
    RouteDTO(
        path="/open",
        endpoint=open_connection,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Открыть соединение",
        description="Открыть логическое соединение с кассовым аппаратом",
        responses={
            status.HTTP_200_OK: {
                "description": "Соединение успешно открыто",
            },
        },
    ),
    RouteDTO(
        path="/close",
        endpoint=close_connection,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Закрыть соединение",
        description="Закрыть логическое соединение с кассовым аппаратом",
        responses={
            status.HTTP_200_OK: {
                "description": "Соединение успешно закрыто",
            },
        },
    ),
    RouteDTO(
        path="/is-opened",
        endpoint=is_connection_opened,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Проверить соединение",
        description="Проверить состояние логического соединения с ККТ",
        responses={
            status.HTTP_200_OK: {
                "description": "Статус соединения получен",
            },
        },
    ),
]
