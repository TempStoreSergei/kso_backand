from fastapi import Depends, Query, Body
from redis.asyncio import Redis

from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.receipt.open_receipt_dto import OpenReceiptRequest
from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.fiscal.DTO.receipt.other_dto import *


async def open_receipt(
    data: OpenReceiptRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "open_receipt",
        "kwargs": data.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def cancel_receipt(
    data: CancelReceiptRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "cancel_receipt",
        "kwargs": data.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def registration(
    data: RegistrationRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "registration",
        "kwargs": data.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def payment(
    data: PaymentRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "payment",
        "kwargs": data.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def receipt_tax(
    data: ReceiptTaxRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "receipt_tax",
        "kwargs": data.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def receipt_total(
    data: ReceiptTotalRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "receipt_total",
        "kwargs": data.model_dump()
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def close_receipt(
    data: CloseReceiptRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "close_receipt",
        "kwargs": data.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def check_document_closed(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "check_document_closed"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def continue_print(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "continue_print"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


# ========== ОПЕРАЦИИ С КОДАМИ МАРКИРОВКИ (ФФД 1.2) ==========

async def begin_marking_code_validation(
    data: BeginMarkingCodeValidationRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "begin_marking_code_validation",
        "kwargs": data.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_marking_code_validation_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_marking_code_validation_status"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def accept_marking_code(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "accept_marking_code"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def decline_marking_code(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "decline_marking_code"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def cancel_marking_code_validation(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "cancel_marking_code_validation"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def clear_marking_code_validation_result(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "clear_marking_code_validation_result"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def check_marking_code_validations_ready(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "check_marking_code_validations_ready"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def write_sales_notice(
    data: WriteSalesNoticeRequest,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "write_sales_notice",
        "kwargs": data.model_dump(exclude_none=True)
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def update_fnm_keys(
    timeout: int = Query(60000, description="Таймаут ожидания обновления в мс"),
    print_report: bool = Query(False, description="Печать отчёта ОКП"),
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "update_fnm_keys",
        "kwargs": {
            "timeout": timeout,
            "print_update_fnm_keys_report": print_report
        }
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def ping_marking_server(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "ping_marking_server"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def get_marking_server_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "get_marking_server_status"
    }
    response = await pubsub_command_util(redis, f"command_fr_channel_{device_id}", command)
    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
