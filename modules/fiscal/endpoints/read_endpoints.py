"""Эндпоинты для чтения данных из ФН и ККТ"""
from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import pubsub_command_util, get_redis
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.DTO.read.read_fn_document_dto import ReadFnDocumentRequestDTO
from modules.fiscal.DTO.read.read_registration_dto import ReadRegistrationDocumentRequestDTO
from modules.fiscal.DTO.read.parse_complex_attr_dto import ParseComplexAttributeRequestDTO
from modules.fiscal.DTO.read.read_settings_dto import ReadSettingsRequestDTO
from modules.fiscal.DTO.read.read_last_document_dto import ReadLastDocumentJournalRequestDTO


async def read_fn_document(
    request: ReadFnDocumentRequestDTO,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Чтение документа из ФН в виде TLV-структур"""
    command = {
        "device_id": device_id,
        "command": "read_fn_document",
        "kwargs": {
            "document_number": request.document_number
        }
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def read_licenses(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Чтение списка введенных лицензий / кодов защиты"""
    command = {
        "device_id": device_id,
        "command": "read_licenses",
        "kwargs": {}
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def read_registration_document(
    request: ReadRegistrationDocumentRequestDTO,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Чтение документа регистрации из ФН в виде TLV-структур"""
    command = {
        "device_id": device_id,
        "command": "read_registration_document",
        "kwargs": {
            "registration_number": request.registration_number
        }
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def parse_complex_attribute(
    request: ParseComplexAttributeRequestDTO,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Разбор составного реквизита"""
    command = {
        "device_id": device_id,
        "command": "parse_complex_attribute",
        "kwargs": {
            "tag_value": request.tag_value
        }
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def read_kkt_settings(
    request: ReadSettingsRequestDTO,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Чтение всех настроек ККТ"""
    command = {
        "device_id": device_id,
        "command": "read_kkt_settings",
        "kwargs": {}
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )


async def read_last_document_journal(
    request: ReadLastDocumentJournalRequestDTO,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """Чтение последнего закрытого документа из электронного журнала"""
    command = {
        "device_id": device_id,
        "command": "read_last_document_journal",
        "kwargs": {}
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=response.get('data'),
    )
