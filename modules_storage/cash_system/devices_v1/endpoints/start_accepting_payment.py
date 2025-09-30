from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.start_accepting_payment_response_dto import \
    StartAcceptingPaymentResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def start_accepting_payment(
    amount: int,
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'start_accepting_payment', 'data': {'amount': amount}}
    response = await pubsub_command_util(
        redis,
        cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
        command,
    )
    return StartAcceptingPaymentResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
