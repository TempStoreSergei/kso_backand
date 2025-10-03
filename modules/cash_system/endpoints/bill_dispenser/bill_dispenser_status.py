from typing import TYPE_CHECKING

from fastapi import Depends

from modules.cash_system.DTO.bill_dispenser.bill_dispenser_status_response_dto import BillDispenserStatusResponseDTO
from api.dependencies.redis_connection import get_redis
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def bill_dispenser_status(
    redis: "Redis" = Depends(get_redis),
):
    upper_box_value = await redis.get('bill_dispenser:upper_lvl') or None
    lower_box_value = await redis.get('bill_dispenser:lower_lvl') or None
    upper_box_count = await redis.get('bill_dispenser:upper_count') or None
    lower_box_count = await redis.get('bill_dispenser:lower_count') or None

    return BillDispenserStatusResponseDTO(
        upper_box_value=upper_box_value,
        lower_box_value=lower_box_value,
        upper_box_count=upper_box_count,
        lower_box_count=lower_box_count,
        upper_cassette_size=cash_system_settings.UPPER_CASSETTE_SIZE,
        lower_cassette_size=cash_system_settings.LOWER_CASSETTE_SIZE,
    )
