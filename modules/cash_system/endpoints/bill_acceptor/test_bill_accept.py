from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.configs.settings import cash_system_settings
from modules.cash_system.DTO.bill_acceptor.test_bill_accept_dto import \
    TestBillAcceptResponseDTO, TestBillAcceptRequestDTO

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def test_bill_accept(
    data: TestBillAcceptRequestDTO,
    redis: "Redis" = Depends(get_redis),
):
    try:
        await redis.set('cash_system_is_test_mode', 'True')

        command = {
            'command': 'start_accepting_payment',
            'data': {'amount': int(data.amount)}
        }

        response = await pubsub_command_util(
            redis,
            cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
            command
        )
    finally:
        await redis.delete('cash_system_is_test_mode')
    return TestBillAcceptResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
    )
