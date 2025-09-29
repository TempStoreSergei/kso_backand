from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.acquiring.DTO.check_connect_response_dto import CheckConnectResponseDTO
from modules.acquiring.configs.settings import acquiring_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def check_connect_old(
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'check_connect_old'}
    response = await pubsub_command_util(
        redis,
        acquiring_settings.ACQUIRING_CHANNEL,
        command,
    )
    return CheckConnectResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
