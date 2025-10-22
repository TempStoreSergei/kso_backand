from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO


async def get_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_status",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_short_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_short_status",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_cash_sum(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_cash_sum",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_shift_state(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_shift_state",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_receipt_state(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_receipt_state",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_datetime(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_datetime",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_serial_number(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_serial_number",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_model_info(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_model_info",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_receipt_line_length(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_receipt_line_length",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_unit_version(
    unit_type: int = Query(
        0,
        description=(
            "Тип модуля: 0=прошивка (FIRMWARE), 1=конфигурация (CONFIGURATION), "
            "2=шаблоны (TEMPLATES), 3=блок управления (CONTROL_UNIT), 4=загрузчик (BOOT)"
        )
    ),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_unit_version",
        "kwargs": {"unit_type": unit_type}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_payment_sum(
    payment_type: int = Query(..., description="Тип оплаты: 0=наличные, 1=безнал, 2=аванс, 3=кредит, 4=иное"),
    receipt_type: int = Query(..., description="Тип чека: 0=продажа, 1=возврат, 2=покупка, 3=возврат покупки"),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_payment_sum",
        "kwargs": {"payment_type": payment_type, "receipt_type": receipt_type}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_cashin_sum(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_cashin_sum",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_cashout_sum(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_cashout_sum",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_receipt_count(
    receipt_type: int = Query(..., description="Тип чека: 0=продажа, 1=возврат, 2=покупка, 3=возврат покупки"),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_receipt_count",
        "kwargs": {"receipt_type": receipt_type}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_non_nullable_sum(
    receipt_type: int = Query(..., description="Тип чека: 0=продажа, 1=возврат, 2=покупка, 3=возврат покупки"),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_non_nullable_sum",
        "kwargs": {"receipt_type": receipt_type}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_power_source_state(
    power_source_type: int = Query(
        2,
        description="Тип источника: 0=блок питания, 1=батарея часов, 2=аккумуляторы"
    ),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_power_source_state",
        "kwargs": {"power_source_type": power_source_type}
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_printer_temperature(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_printer_temperature",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_fatal_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_fatal_status",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_mac_address(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_mac_address",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_ethernet_info(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_ethernet_info",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_wifi_info(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_wifi_info",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def query_last_receipt(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_last_receipt",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def query_registration_info(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_registration_info",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def query_fn_info(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_fn_info",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def query_ofd_exchange_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_ofd_exchange_status",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def query_shift_info(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_shift_info",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def query_last_document(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_last_document",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def query_fn_validity(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "query_fn_validity",
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
