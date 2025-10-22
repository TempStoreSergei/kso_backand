from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.endpoints.config_endpoints import *


CONFIG_ROUTES = [
    RouteDTO(
        path="/logging",
        endpoint=configure_logging,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Настроить логирование",
        description="Настроить логирование драйвера АТОЛ",
        responses={
            status.HTTP_200_OK: {
                "description": "Логирование успешно настроено",
            },
        },
    ),
    RouteDTO(
        path="/label",
        endpoint=change_driver_label,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Изменить метку драйвера",
        description="Изменить метку драйвера для логирования",
        responses={
            status.HTTP_200_OK: {
                "description": "Метка драйвера успешно изменена",
            },
        },
    ),
    RouteDTO(
        path="/logging/defaults",
        endpoint=get_default_logging_config,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Настройки логирования по умолчанию",
        description="Получить настройки логирования по умолчанию",
        responses={
            status.HTTP_200_OK: {
                "description": "Настройки логирования получены",
            },
        },
    ),
]
