from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.acquiring.DTO.start_payment_response_dto import StartPaymentResponseDTO
from modules.acquiring.configs.settings import acquiring_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def start_payment(
    amount: int,
    redis: "Redis" = Depends(get_redis),
):
    command = {
        'command': 'start_pay',
        'data': {'amount': amount},
    }
    response = await pubsub_command_util(
        redis,
        acquiring_settings.ACQUIRING_CHANNEL,
        command,
    )
    return StartPaymentResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
