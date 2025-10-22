from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.cash.cash_in_dto import CashOperationRequest


async def cash_in(
    request: CashOperationRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "cash_in",
        "kwargs": request.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def cash_out(
    request: CashOperationRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "cash_out",
        "kwargs": request.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
            success=response.get('success'),
            message=response.get('message'),
        )


async def get_cash_sum(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_data",
        "kwargs": {"data_type": 3}  # LIBFPTR_DT_CASH_SUM = 3
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
            success=response.get('success'),
            message=response.get('message'),
        )


async def open_cash_drawer(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "cash_drawer_open"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_cash_drawer_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_data",
        "kwargs": {"data_type": 1}  # LIBFPTR_DT_STATUS = 1
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
