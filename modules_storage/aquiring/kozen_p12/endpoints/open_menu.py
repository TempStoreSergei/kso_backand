from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.acquiring.DTO.open_menu_response_dto import OpenMenuResponseDTO
from modules.acquiring.configs.settings import acquiring_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def open_menu(
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'open_menu'}
    response = await pubsub_command_util(
        redis,
        acquiring_settings.ACQUIRING_CHANNEL,
        command,
    )
    return OpenMenuResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
