from typing import TYPE_CHECKING, Literal

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.coin_system.test_coin_accept_response_dto import \
    TestCoinAcceptResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def test_coin_accept(
    amount: Literal[1, 2, 5, 10],
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'coin_system_add_coin_count', 'data': {'amount': amount}}
    response = await pubsub_command_util(
        redis,
        cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
        command,
    )
    return TestCoinAcceptResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
