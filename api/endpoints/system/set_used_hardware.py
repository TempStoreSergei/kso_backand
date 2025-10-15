from fastapi import Depends

from typing import TYPE_CHECKING

from api.DTO.system.set_used_hadrware_dto import SetUsedHardwareRequestDTO, \
    SetUsedHardwareResponseDTO
from api.dependencies.redis_connection import get_redis

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def set_used_hardware(data: SetUsedHardwareRequestDTO,redis: "Redis" = Depends(get_redis)):
    # Проверяем тип ключа и удаляем, если он не является множеством
    key_name = "used_hardware"
    key_type = await redis.type(key_name)
    if key_type != b'set':  # Redis возвращает тип в виде bytes
        await redis.delete(key_name)

    # Добавляем устройства в множество
    for device in data.devices:
        await redis.sadd(key_name, device.value)
    return SetUsedHardwareResponseDTO(detail='Настройки установлены успешно')
