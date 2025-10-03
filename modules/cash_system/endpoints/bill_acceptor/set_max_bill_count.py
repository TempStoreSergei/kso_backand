from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis
from modules.cash_system.DTO.bill_acceptor.set_max_bill_count_response_dto import \
    SetMaxBillCountResponseDTO

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def set_max_bill_count(
    value: int,
    redis: "Redis" = Depends(get_redis),
):
    await redis.set('max_bill_count', value)
    return SetMaxBillCountResponseDTO(
        detail='Максимальное значение кол-ва купюр установлено успешно',
    )
