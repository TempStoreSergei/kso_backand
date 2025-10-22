from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.shift.open_shift_dto import OpenShiftRequest


async def open_shift(
    data: OpenShiftRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Открыть новую смену"""
    kwargs = {}
    if data.cashier_name:
        kwargs["cashier_name"] = data.cashier_name
    if data.cashier_inn:
        kwargs["cashier_inn"] = data.cashier_inn

    command = {
        "device_id": device_id,
        "command": "open_shift",
        "kwargs": kwargs
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def close_shift(
    cashier_name: str = Query(None, description="Имя кассира (если не указано, используется из настроек)"),
    cashier_inn: str = Query(None, description="ИНН кассира (если не указано, используется из настроек)"),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Закрыть текущую смену (Z-отчет)"""
    kwargs = {}
    if cashier_name:
        kwargs["cashier_name"] = cashier_name
    if cashier_inn:
        kwargs["cashier_inn"] = cashier_inn

    command = {
        "device_id": device_id,
        "command": "close_shift",
        "kwargs": kwargs
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
        "command": "get_shift_status"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def print_x_report(
    cashier_name: str = Query(None, description="Имя кассира (если не указано, используется из настроек)"),
    cashier_inn: str = Query(None, description="ИНН кассира (если не указано, используется из настроек)"),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Напечатать X-отчет (отчет без гашения)"""
    kwargs = {}
    if cashier_name:
        kwargs["cashier_name"] = cashier_name
    if cashier_inn:
        kwargs["cashier_inn"] = cashier_inn

    command = {
        "device_id": device_id,
        "command": "print_x_report",
        "kwargs": kwargs
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
