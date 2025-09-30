from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.acquiring.DTO.receipt_report_response_dto import ReceiptReportResponseDTO
from modules.acquiring.configs.settings import acquiring_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def receipt_report(
    redis: "Redis" = Depends(get_redis),
):
    command = {'command': 'receipt_report'}
    response = await pubsub_command_util(
        redis,
        acquiring_settings.ACQUIRING_CHANNEL,
        command,
    )
    return ReceiptReportResponseDTO(
        status=response.get('success'),
        detail=response.get('message'),
        data=response.get('data')
    )
