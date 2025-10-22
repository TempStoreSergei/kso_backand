from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.endpoints.operator_endpoints import *


OPERATOR_ROUTES = [
    RouteDTO(
        path="/login",
        endpoint=operator_login,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Регистрация кассира",
        description="Зарегистрировать кассира (operatorLogin)",
        responses={
            status.HTTP_200_OK: {
                "description": "Кассир успешно зарегистрирован",
            },
        },
    ),
    RouteDTO(
        path="/continue-ttt",
        endpoint=continue_print,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Допечатать документ",
        description="Допечатать документ (continuePrint)",
        responses={
            status.HTTP_200_OK: {
                "description": "Документ допечатан",
            },
        },
    ),
    RouteDTO(
        path="/check-document-closed",
        endpoint=check_document_closed,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Проверить закрытие документа",
        description="Проверить закрытие документа (checkDocumentClosed)",
        responses={
            status.HTTP_200_OK: {
                "description": "Состояние документа проверено",
            },
        },
    ),
]
