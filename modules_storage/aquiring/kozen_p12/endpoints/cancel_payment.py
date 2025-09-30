from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.acquiring.DTO.cancel_pay_response_dto import CancelPaymentResponseDTO
from modules.acquiring.configs.settings import acquiring_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def cancel_payment(
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'cancel_pay'}
    response = await pubsub_command_util(
        redis,
        acquiring_settings.ACQUIRING_CHANNEL,
        command,
    )
    return CancelPaymentResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
        data=response.get('data')
    )
