from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.endpoints.cash_endpoints import *


CASH_ROUTES = [
    RouteDTO(
        path="/in",
        endpoint=cash_in,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Внесение наличных",
        description="Внесение наличных в кассу",
        responses={
            status.HTTP_200_OK: {
                "description": "Наличные успешно внесены",
            },
        },
    ),
    RouteDTO(
        path="/out",
        endpoint=cash_out,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Изъятие наличных",
        description="Изъятие наличных из кассы",
        responses={
            status.HTTP_200_OK: {
                "description": "Наличные успешно изъяты",
            },
        },
    ),
    RouteDTO(
        path="/sum",
        endpoint=get_cash_sum,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Сумма в ящике",
        description="Получить сумму наличных в денежном ящике",
        responses={
            status.HTTP_200_OK: {
                "description": "Сумма наличных получена",
            },
        },
    ),
    RouteDTO(
        path="/drawer/open",
        endpoint=open_cash_drawer,
        response_model=None,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Открыть ящик",
        description="Открыть денежный ящик.\n\nПодает сигнал на открытие денежного ящика, подключенного к ККТ.",
        responses={
            status.HTTP_200_OK: {
                "description": "Денежный ящик открыт",
            },
        },
    ),
    RouteDTO(
        path="/drawer/status",
        endpoint=get_cash_drawer_status,
        response_model=None,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Статус ящика",
        description="Проверить состояние денежного ящика",
        responses={
            status.HTTP_200_OK: {
                "description": "Статус денежного ящика получен",
            },
        },
    ),
]
