from typing import TYPE_CHECKING

from fastapi import Depends

from api.DTO.notifications.tg_bot_notifications_dto import TgBotNotificationsRequestDTO, \
    TgBotNotificationsResponseDTO
from api.dependencies.redis_connection import get_redis

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def start_tg_bot_notifications(
    bot_data: TgBotNotificationsRequestDTO,
    redis: "Redis" = Depends(get_redis),
):
    await redis.set('tg_bot_notifications:token', bot_data.token)
    await redis.set('tg_bot_notifications:chat_id', bot_data.chat)

    return TgBotNotificationsResponseDTO(detail='Данные бота добавлены успешно')
