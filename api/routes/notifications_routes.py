from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from api.DTO.notifications.tg_bot_notifications_dto import TgBotNotificationsResponseDTO
from api.endpoints.notifications.start_tg_bot_notifications import start_tg_bot_notifications
from api.endpoints.notifications.stop_tg_bot_notifications import stop_tg_bot_notifications

NOTIFICATIONS_ROUTES = [
    RouteDTO(
        path="/tg/start",
        endpoint=start_tg_bot_notifications,
        response_model=TgBotNotificationsResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/tg/stop",
        endpoint=stop_tg_bot_notifications,
        response_model=TgBotNotificationsResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]