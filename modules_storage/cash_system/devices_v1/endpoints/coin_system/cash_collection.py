from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.coin_system.cash_collection_response_dto import \
    CashCollectionResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def cash_collection(
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'coin_system_cash_collection'}
    response = await pubsub_command_util(
        redis,
        cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
        command,
    )
    return CashCollectionResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
