from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.configs.settings import cash_system_settings
from modules.cash_system.DTO.bill_acceptor.set_max_bill_count_response_dto import \
    SetMaxBillCountResponseDTO

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def set_max_bill_count(
    value: int,
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'bill_acceptor_set_max_bill_count', 'data': {'value': value}}
    response = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command
    )
    return SetMaxBillCountResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
