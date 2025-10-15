from fastapi import Depends, HTTPException, status
import httpx

from typing import TYPE_CHECKING

from api.DTO.system.check_system_dto import CheckSystemResponseDTO, DeviceCheckSystemResponseDTO
from api.dependencies.redis_connection import get_redis, pubsub_command_util

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def check_system(redis: "Redis" = Depends(get_redis)):
    used_hardware = await redis.smembers('used_hardware')

    if not used_hardware:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Система не настроена, необходимо настроить оборудование'
        )

    fiscal = None
    acquiring = None
    scanner = None

    async with httpx.AsyncClient(base_url='http://localhost:8005/api/v1', timeout=5) as client:
        if 'fiscal' in used_hardware:
            fiscal = DeviceCheckSystemResponseDTO(
                connect=False,
                detail='',
            )

        if 'acquiring' in used_hardware:
            try:
                response = await client.get('/acquiring/check_connect')
                acquiring = DeviceCheckSystemResponseDTO(
                    connect=response.json().get('status'),
                    detail=response.json().get('detail'),
                )
            except httpx.TimeoutException:
                acquiring = DeviceCheckSystemResponseDTO(
                    connect=False,
                    detail='Таймаут ответа от устройства'
                )

        if 'scanner' in used_hardware:
            response = await client.get('/scanner/check_scanner_service')
            scanner = DeviceCheckSystemResponseDTO(
                connect=response.json().get('status'),
                detail=response.json().get('detail'),
            )

    return CheckSystemResponseDTO(
        fiscal=fiscal,
        acquiring=acquiring,
        scanner=scanner,
    )