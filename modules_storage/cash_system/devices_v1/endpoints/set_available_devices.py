from typing import TYPE_CHECKING

from fastapi import Depends

from api.dependencies.redis_connection import get_redis
from modules.cash_system.DTO.set_available_devices_dto import SetAvailableDevicesRequestDTO, \
    SetAvailableDevicesResponseDTO

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def set_available_devices(
    data: SetAvailableDevicesRequestDTO,
    redis: "Redis" = Depends(get_redis),
):
    devices_lst = []
    if data.bill_acceptor:
        devices_lst.append('bill_acceptor')
    if data.bill_dispenser:
        devices_lst.append('bill_dispenser')
    if data.coin_acceptor:
        devices_lst.append('coin_acceptor')

    await redis.delete("available_devices_cash")
    await redis.sadd("available_devices_cash", *devices_lst)
    return SetAvailableDevicesResponseDTO(
        detail=f'Устройства наличной платежной системы установлены успешно: {devices_lst}'
    )
