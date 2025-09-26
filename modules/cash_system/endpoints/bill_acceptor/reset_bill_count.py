from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.configs.settings import cash_system_settings
from modules.cash_system.DTO.bill_acceptor.reset_bill_count_response_dto import \
    ResetBillCountResponseDTO

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def reset_bill_count(
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'bill_acceptor_reset_bill_count'}
    response = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command
    )
    return ResetBillCountResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
