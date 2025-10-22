from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.shift.open_shift_dto import OpenShiftRequest


async def open_shift(
    request: OpenShiftRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Открыть новую смену"""
    command = {
        "device_id": device_id,
        "command": "shift_open",
        "kwargs": {"cashier_name": request.cashier_name}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def close_shift(
    cashier_name: str,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Закрыть текущую смену (Z-отчет)"""
    command = {
        "device_id": device_id,
        "command": "shift_close",
        "kwargs": {"cashier_name": cashier_name}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_shift_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Получить статус текущей смены"""
    command = {
        "device_id": device_id,
        "command": "shift_get_status"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def print_x_report(
    cashier_name: str,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Напечатать X-отчет (отчет без гашения)"""
    command = {
        "device_id": device_id,
        "command": "shift_print_x_report",
        "kwargs": {"cashier_name": cashier_name}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
