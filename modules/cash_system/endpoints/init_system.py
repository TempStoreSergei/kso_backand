from typing import TYPE_CHECKING

from fastapi import Depends

from modules.cash_system.DTO.init_system_response_dto import InitSystemResponseDTO
from api.dependencies.get_current_user import get_current_user
from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from api.models.auth_models import User
    from redis.asyncio import Redis


async def init_system(
    user: "User" = Depends(get_current_user),
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'init_devices'}
    response = await pubsub_command_util(
        redis,
        cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
        command,
    )
    return InitSystemResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
