from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.bill_dispenser.set_nominal_dto import SetNominalRequestDTO, \
    SetNominalResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def set_nominal(nominals: SetNominalRequestDTO, redis: "Redis" = Depends(get_redis)):
    command = {
        'command': 'set_bill_dispenser_lvl',
        'data': {'upper_lvl': nominals.upper_lvl, 'lower_lvl': nominals.lower_lvl}
    }
    response = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command
    )
    return SetNominalResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
