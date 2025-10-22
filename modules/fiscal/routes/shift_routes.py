from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.endpoints.shift_endpoints import *


SHIFT_ROUTES = [
    RouteDTO(
        path="/open",
        endpoint=open_shift,
        response_model=None,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Открыть смену",
        description="Открыть новую смену",
        responses={
            status.HTTP_200_OK: {
                "description": "Смена успешно открыта",
            },
        },
    ),
    RouteDTO(
        path="/close",
        endpoint=close_shift,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Закрыть смену",
        description="Закрыть текущую смену (Z-отчет)",
        responses={
            status.HTTP_200_OK: {
                "description": "Смена успешно закрыта, Z-отчет сформирован",
            },
        },
    ),
    RouteDTO(
        path="/status",
        endpoint=get_shift_status,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Статус смены",
        description="Получить статус текущей смены",
        responses={
            status.HTTP_200_OK: {
                "description": "Статус смены получен",
            },
        },
    ),
    RouteDTO(
        path="/x-report",
        endpoint=print_x_report,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="X-отчет",
        description="Напечатать X-отчет (отчет без гашения)",
        responses={
            status.HTTP_200_OK: {
                "description": "X-отчет успешно напечатан",
            },
        },
    ),
]
