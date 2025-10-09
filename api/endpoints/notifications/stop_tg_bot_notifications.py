from typing import TYPE_CHECKING

from fastapi import Depends

from api.DTO.notifications.tg_bot_notifications_dto import TgBotNotificationsResponseDTO
from api.dependencies.redis_connection import get_redis

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def stop_tg_bot_notifications(redis: "Redis" = Depends(get_redis)):
    await redis.delete('tg_bot_notifications:token')
    await redis.delete('tg_bot_notifications:chat_id')

    return TgBotNotificationsResponseDTO(detail='Данные бота удалены успешно')
