from typing import TYPE_CHECKING

from fastapi import Depends, HTTPException

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.DTO.coin_system.add_coin_count_dto import AddCoinCountRequestDTO, \
    AddCoinCountResponseDTO
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from redis.asyncio import Redis


async def add_coin_count(
    data: AddCoinCountRequestDTO,
    redis: "Redis" = Depends(get_redis),
):
    values = []
    denominations = []
    if data.coin_100:
        denominations.append(100)
        values.append(data.coin_100)
    if data.coin_200:
        denominations.append(200)
        values.append(data.coin_200)
    if data.coin_500:
        denominations.append(500)
        values.append(data.coin_500)
    if data.coin_1000:
        denominations.append(1000)
        values.append(data.coin_1000)

    for value, denomination in zip(values, denominations):
        command = {
            'command': 'coin_system_add_coin_count',
            'data': {'value': value, 'denomination': denomination},
        }
        response = await pubsub_command_util(
            redis,
            cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
            command,
        )
        if not response.get('success'):
            raise HTTPException(
                400,
                f'Ошибка при установке уровня монет для номинала {denomination}',
            )

    command = {'command': 'coin_system_status'}
    response = await pubsub_command_util(
        redis,
        cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL,
        command,
    )
    response_data = response.get('data')
    return AddCoinCountResponseDTO(
        coin_100=response_data.get('100'),
        coin_200=response_data.get('200'),
        coin_500=response_data.get('500'),
        coin_1000=response_data.get('1000'),
    )
