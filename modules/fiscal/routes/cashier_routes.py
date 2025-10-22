from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.endpoints.cashier_endpoints import set_cashier, get_cashier, reset_cashier


CASHIER_ROUTES = [
    RouteDTO(
        path="/set",
        endpoint=set_cashier,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Установить текущего кассира",
        description="Установить кассира для устройства. Кассир будет использоваться по умолчанию для всех операций, "
                    "пока не будет изменен или сброшен. Параметры передаются в теле запроса.",
        responses={
            status.HTTP_200_OK: {
                "description": "Кассир успешно установлен",
            },
        },
    ),
    RouteDTO(
        path="/current",
        endpoint=get_cashier,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Получить текущего кассира",
        description="Получить текущего кассира для устройства. "
                    "Возвращает динамически установленного кассира или кассира из настроек.",
        responses={
            status.HTTP_200_OK: {
                "description": "Информация о текущем кассире получена",
            },
        },
    ),
    RouteDTO(
        path="/reset",
        endpoint=reset_cashier,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Сбросить текущего кассира",
        description="Сбросить динамически установленного кассира. "
                    "После сброса будет использоваться кассир из настроек (.env файла).",
        responses={
            status.HTTP_200_OK: {
                "description": "Кассир успешно сброшен",
            },
        },
    ),
]
