from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.stop_accepting_payment_response_dto import \
    StopAcceptingPaymentResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def stop_accepting_payment(
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'stop_accepting_payment'}
    response = await pubsub_command_util(
        redis,
        cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
        command,
    )
    return StopAcceptingPaymentResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
