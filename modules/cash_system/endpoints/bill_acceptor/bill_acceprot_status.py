from typing import TYPE_CHECKING

from fastapi import Depends

from modules.cash_system.DTO.bill_acceptor.bill_acceprot_status_response_dto import BillAcceptorStatusResponseDTO
from api.dependencies.redis_connection import get_redis
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def bill_acceptor_status(
    redis: "Redis" = Depends(get_redis),
):
    max_bill_count = await redis.get('max_bill_count') or None
    bill_count = await redis.get('bill_count') or None

    return BillAcceptorStatusResponseDTO(
        cassette_size=cash_system_settings.CASSETTE_SIZE,
        max_bill_count=max_bill_count,
        bill_count=bill_count,
    )
