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
        description="Зарегистрировать кассира перед выполнением фискальной операции. Рекомендуется вызывать перед каждой операцией (открытие чека, печать отчета и т.д.)",
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
        description="Допечатать фискальный документ, который не был допечатан из-за проблем с принтером (закончилась бумага, открыта крышка и т.д.)",
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
        description="Проверить, был ли документ успешно закрыт в ФН и напечатан на чековой ленте. Важнейший метод для обеспечения надежности!",
        responses={
            status.HTTP_200_OK: {
                "description": "Состояние документа проверено",
            },
        },
    ),
]
