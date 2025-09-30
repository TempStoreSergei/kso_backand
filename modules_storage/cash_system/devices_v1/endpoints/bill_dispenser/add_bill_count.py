from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.bill_dispenser.add_bill_count_dto import AddBillCountRequestDTO, \
    AddBillCountResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def add_bill_count(data: AddBillCountRequestDTO, redis: "Redis" = Depends(get_redis)):
    command = {
        'command': 'set_bill_dispenser_count',
        'data': {'upper_count': data.upper_count, 'lower_count': data.lower_count}
    }
    response = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command
    )
    return AddBillCountResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
