"""Эндпоинты для управления текущим кассиром"""
from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import get_redis
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.cashier.cashier_dto import SetCashierRequest, CashierInfoDTO
from api.configs.settings import settings


async def set_cashier(
    request: SetCashierRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Установить текущего кассира для устройства.

    Кассир будет использоваться по умолчанию для всех операций на этом устройстве,
    пока не будет изменен или сброшен.
    """
    # Сохраняем кассира в Redis
    cashier_key = f"cashier:{device_id}"
    cashier_data = {
        "cashier_name": request.cashier_name,
        "cashier_inn": request.cashier_inn or ""
    }

    await redis.hset(cashier_key, mapping=cashier_data)

    return BaseResponseDTO(
        success=True,
        message=f"Кассир '{request.cashier_name}' успешно установлен для устройства {device_id}",
        data=cashier_data
    )


async def get_cashier(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Получить текущего кассира для устройства.

    Возвращает динамически установленного кассира или кассира из настроек.
    """
    # Проверяем есть ли кассир в Redis
    cashier_key = f"cashier:{device_id}"
    cashier_data = await redis.hgetall(cashier_key)

    if cashier_data:
        # Есть динамический кассир
        return BaseResponseDTO(
            success=True,
            message="Текущий кассир (динамический)",
            data={
                "cashier_name": cashier_data.get(b"cashier_name", b"").decode('utf-8'),
                "cashier_inn": cashier_data.get(b"cashier_inn", b"").decode('utf-8'),
                "source": "dynamic"
            }
        )
    else:
        # Используем кассира из настроек
        return BaseResponseDTO(
            success=True,
            message="Текущий кассир (из настроек)",
            data={
                "cashier_name": settings.cashier_name,
                "cashier_inn": settings.cashier_inn,
                "source": "settings"
            }
        )


async def reset_cashier(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Сбросить текущего кассира.

    После сброса будет использоваться кассир из настроек.
    """
    cashier_key = f"cashier:{device_id}"
    await redis.delete(cashier_key)

    return BaseResponseDTO(
        success=True,
        message=f"Кассир для устройства {device_id} сброшен, будет использоваться кассир из настроек",
        data={
            "cashier_name": settings.cashier_name,
            "cashier_inn": settings.cashier_inn,
            "source": "settings"
        }
    )
