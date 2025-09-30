from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.coin_system.test_coin_dispense_response_dto import \
    TestCoinDispenseResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def test_coin_dispense(
    redis: "Redis" = Depends(get_redis),
):
    command = {
        'command': 'test_dispense_change',
        'data': {'is_bill': False, 'is_coin': True},
    }
    response = await pubsub_command_util(
        redis,
        cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
        command,
    )
    return TestCoinDispenseResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
