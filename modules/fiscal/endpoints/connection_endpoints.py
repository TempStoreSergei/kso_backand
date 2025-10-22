from fastapi import Depends, Query
from redis.asyncio import Redis

from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.connection.open_connection_dto import OpenConnectionRequest
from api.dependencies.redis_connection import get_redis, pubsub_command_util


async def open_connection(
    request: OpenConnectionRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Открыть логическое соединение с ККТ"""
    command = {
        "device_id": device_id,
        "command": "connection_open",
        "kwargs": {"settings": request.settings}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def close_connection(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Закрыть логическое соединение с ККТ"""
    command = {
        "device_id": device_id,
        "command": "connection_close"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def is_connection_opened(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Проверить состояние логического соединения"""
    command = {
        "device_id": device_id,
        "command": "connection_is_opened"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
