from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.acquiring.DTO.refund_payment_response_dto import RefundPaymentResponseDTO
from modules.acquiring.configs.settings import acquiring_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def refund_payment(
    amount: int,
    redis: "Redis" = Depends(get_redis),
):
    command = {
        'command': 'refund_pay',
        'data': {'amount': amount},
    }
    response = await pubsub_command_util(
        redis,
        acquiring_settings.ACQUIRING_CHANNEL,
        command,
    )
    return RefundPaymentResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
        data=response.get('data')
    )
