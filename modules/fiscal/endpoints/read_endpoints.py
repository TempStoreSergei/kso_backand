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


def decode_bytes_to_string(byte_array: list[int]) -> str:
    """
    Преобразует массив байтов в читаемую строку.
    Пробует разные кодировки: CP866 (для кириллицы ККТ), UTF-8, ASCII.
    """
    if not isinstance(byte_array, list):
        return str(byte_array)

    try:
        # Преобразуем список байтов в bytes
        byte_string = bytes(byte_array)

        # Пробуем CP866 (основная кодировка для ККТ АТОЛ)
        try:
            decoded = byte_string.decode('cp866').strip()
            if decoded:
                return decoded
        except:
            pass

        # Пробуем UTF-8
        try:
            decoded = byte_string.decode('utf-8').strip()
            if decoded:
                return decoded
        except:
            pass

        # Пробуем ASCII
        try:
            decoded = byte_string.decode('ascii').strip()
            if decoded:
                return decoded
        except:
            pass

        # Если не удалось декодировать, возвращаем как hex-строку
        return byte_string.hex()
    except:
        return str(byte_array)


def decode_tlv_records(tlv_records: list[dict]) -> list[dict]:
    """
    Декодирует значения TLV-записей в читаемый вид.
    Преобразует массивы байтов в строки для текстовых полей.
    """
    if not tlv_records:
        return tlv_records

    decoded_records = []
    for record in tlv_records:
        decoded_record = record.copy()
        tag_value = record.get('tag_value')
        tag_type = record.get('tag_type')

        # tag_type == 1 это LIBFPTR_TAG_TYPE_STRING (байтовый массив, обычно текст)
        # tag_type == 4 это LIBFPTR_TAG_TYPE_BITS (битовая маска)
        # tag_type == 6 это LIBFPTR_TAG_TYPE_VLN (переменная длина число)
        # tag_type == 7 это LIBFPTR_TAG_TYPE_UINT_16 (16-битное число)
        # tag_type == 8 это LIBFPTR_TAG_TYPE_UINT_32 (32-битное число)
        # tag_type == 9 это LIBFPTR_TAG_TYPE_UNIXTIME (Unix timestamp)

        if tag_type == 1 and isinstance(tag_value, list):
            # Декодируем байтовый массив в строку
            decoded_record['tag_value'] = decode_bytes_to_string(tag_value)
            decoded_record['tag_value_raw'] = tag_value  # Сохраняем исходные байты
        elif tag_type == 4 and isinstance(tag_value, list):
            # Для битовых масок показываем hex
            decoded_record['tag_value'] = bytes(tag_value).hex()
            decoded_record['tag_value_raw'] = tag_value
        elif tag_type in (6, 7, 8) and isinstance(tag_value, list):
            # VLN, UINT_16, UINT_32 - декодируем в число (little-endian)
            try:
                num_value = int.from_bytes(bytes(tag_value), byteorder='little', signed=False)
                decoded_record['tag_value'] = num_value
                decoded_record['tag_value_raw'] = tag_value
            except:
                # Если не удалось декодировать, оставляем как есть
                pass
        elif tag_type == 9 and isinstance(tag_value, list):
            # UNIX_TIME - декодируем в timestamp и дату
            try:
                timestamp = int.from_bytes(bytes(tag_value), byteorder='little', signed=False)
                import datetime
                dt = datetime.datetime.fromtimestamp(timestamp)
                decoded_record['tag_value'] = timestamp
                decoded_record['tag_value_datetime'] = dt.isoformat()
                decoded_record['tag_value_raw'] = tag_value
            except:
                decoded_record['tag_value_raw'] = tag_value

        decoded_records.append(decoded_record)

    return decoded_records


async def read_fn_document(
    request: ReadFnDocumentRequestDTO,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    command = {
        "device_id": device_id,
        "command": "read_fn_document",
        "kwargs": {
            "document_number": request.document_number
        }
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    # Декодируем TLV-записи для читаемости
    data = response.get('data')
    if data and 'tlv_records' in data:
        data['tlv_records'] = decode_tlv_records(data['tlv_records'])

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=data,
    )


async def read_licenses(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
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
    command = {
        "device_id": device_id,
        "command": "read_registration_document",
        "kwargs": {
            "registration_number": request.registration_number
        }
    }

    channel = f"command_fr_channel_{device_id}"
    response = await pubsub_command_util(redis, channel, command)

    # Декодируем TLV-записи для читаемости
    data = response.get('data')
    if data and 'tlv_records' in data:
        data['tlv_records'] = decode_tlv_records(data['tlv_records'])

    return BaseResponseDTO(
        success=response.get('success'),
        message=response.get('message'),
        data=data,
    )


async def parse_complex_attribute(
    request: ParseComplexAttributeRequestDTO,
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
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
