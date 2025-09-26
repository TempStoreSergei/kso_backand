from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.configs.settings import cash_system_settings
from modules.cash_system.DTO.bill_acceptor.test_bill_accept_response_dto import \
    TestBillAcceptResponseDTO

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def test_bill_accept(
    amount: int,
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'start_accepting_payment', 'data': {
        'amount': amount
    }}
    response = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command
    )
    return TestBillAcceptResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
