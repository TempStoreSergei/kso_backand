from fastapi import Depends, Query
from redis.asyncio import Redis

from modules.fiscal.DTO.config.change_driver_label_dto import ChangeLabelRequest
from modules.fiscal.DTO.config.configure_logging_dto import LoggingConfigRequest
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from api.dependencies.redis_connection import get_redis, pubsub_command_util


async def configure_logging(
    request: LoggingConfigRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "configure_logging",
        "kwargs": request.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def change_driver_label(
    request: ChangeLabelRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "change_driver_label",
        "kwargs": request.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_default_logging_config(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_default_logging_config"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
