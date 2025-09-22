from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.cash_system.DTO.status_system_response_dto import StatusSystemResponseDTO
from modules.cash_system.endpoints.init_system import init_system
from modules.cash_system.DTO.init_system_response_dto import InitSystemResponseDTO
from modules.cash_system.endpoints.status_system import status_system

CASH_SYSTEM_ROUTES = [
    RouteDTO(
        path="/init_system",
        endpoint=init_system,
        response_model=InitSystemResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Инициализация наличной системы оплаты",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/status_system",
        endpoint=status_system,
        response_model=StatusSystemResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Статус системы",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
