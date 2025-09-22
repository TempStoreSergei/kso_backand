from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.get_current_user import get_current_user
from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.bill_dispenser.test_bill_dispense_response_DTO import \
    TestBillDispenseResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from api.models.auth_models import User
    from redis.asyncio import Redis


async def test_bill_dispense(
    amount: int,
    user: "User" = Depends(get_current_user),
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'test_dispense_change'}
    response = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command
    )
    return TestBillDispenseResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
