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
    """Открыть новый чек"""
    command = {
        "device_id": device_id,
        "command": "receipt_open",
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
    """
    Отменить открытый чек.

    Параметр clear_marking_table позволяет не очищать таблицу КМ драйвера,
    если планируется сразу провести точно такой же чек.
    """
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
    """
    Зарегистрировать позицию в чеке.

    Поддерживает:
    - Простые позиции с НДС
    - Позиции с маркировкой (ФФД < 1.2 и ФФД ≥ 1.2)
    - Позиции с агентами и поставщиками
    - Позиции с кодами товара (тег 1163)
    - Позиции с отраслевым реквизитом (тег 1260)
    """
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
    """
    Зарегистрировать оплату чека.

    Поддерживаемые способы оплаты:
    - Наличными (0)
    - Безналичными (1) - с возможностью передачи дополнительных сведений
    - Предварительная оплата/аванс (2)
    - Последующая оплата/кредит (3)
    - Иная форма оплаты (4)
    - Способы расчета №6-10 (5-9)

    Для безналичной оплаты можно передать дополнительные сведения через
    параметры electronically_*.
    """
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
    """
    Зарегистрировать налог на чек.

    Используется когда при регистрации позиций был установлен параметр
    use_only_tax_type=true.
    """
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
    """
    Зарегистрировать итог чека.

    Необязательный метод. Если не вызвать, сумма чека будет посчитана автоматически.
    Можно зарегистрировать итог с округлением в пределах ±99 копеек.
    """
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
    """
    Закрыть чек.

    Если чек не полностью оплачен, будет автоматически доплачен указанным
    способом оплаты (по умолчанию наличными).

    ВАЖНО: После закрытия чека обязательно вызовите check_document_closed()
    для проверки успешности операции!
    """
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
    """
    Проверить закрытие документа.

    КРИТИЧЕСКИ ВАЖНЫЙ метод! Проверяет:
    - Закрылся ли документ в ФН
    - Напечатался ли документ на чековой ленте

    Если документ закрылся, но не напечатался - вызовите continue_print().
    Если документ не закрылся - отмените чек и сформируйте заново.

    Если метод вернул ошибку - нельзя выключать ПК, нужно восстановить работу ККТ!
    """
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
    """
    Допечатать фискальный документ.

    Используется когда документ закрылся в ФН, но не напечатался
    на чековой ленте (например, закончилась бумага).
    """
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
    """
    Начать проверку кода маркировки.

    Режимы работы:
    - Асинхронный (timeout=0): метод не блокируется, нужно опрашивать статус через get_marking_code_validation_status()
    - Синхронный (timeout>0): метод блокируется до завершения проверки или таймаута

    После успешной проверки нужно вызвать:
    - accept_marking_code() для подтверждения реализации
    - decline_marking_code() для отказа от реализации
    - cancel_marking_code_validation() для отмены проверки
    """
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
    """
    Получить статус проверки кода маркировки.

    В асинхронном режиме: вызывать до тех пор, пока validation_ready не станет true.
    В синхронном режиме: вызвать один раз для получения результата.
    """
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
    """
    Подтвердить реализацию товара с кодом маркировки.

    Вызывается после успешной проверки КМ.
    """
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
    """
    Отказаться от реализации товара с кодом маркировки.

    Вызывается после проверки КМ, если товар не будет реализован.
    """
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
    """
    Отменить проверку кода маркировки.

    Можно вызвать на любом этапе проверки для немедленной отмены.
    """
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
    """
    Очистить таблицу проверенных кодов маркировки в ФН.
    """
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
    """
    Проверить завершение всех фоновых проверок КМ.

    Вызывается перед закрытием чека, если были запущены проверки КМ
    без ожидания результата.
    """
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
    """
    Передать данные уведомления о реализации маркированного товара.

    Условия вызова:
    - В чеке должны быть позиции с КМ
    - Вызывать только после регистрации всех позиций
    - Вызывать только до регистрации оплаты, налога, итога или закрытия чека

    Можно передать:
    - ИНН клиента (тег 1228)
    - Отраслевые реквизиты чека (тег 1261, можно несколько)
    - Часовую зону (тег 1011) - ОБЯЗАТЕЛЬНО для маркированных товаров!
    """
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
    """
    Обновить ключи проверки ФН-М.

    Метод блокирующий, выполняется до полного обновления ключей или таймаута.
    Поддерживается только для ККТ версий 5.X, работающих по ФФД ≥ 1.2.
    """
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
    """
    Начать проверку связи с сервером ИСМ.

    После вызова нужно опрашивать get_marking_server_status() до завершения проверки.
    Поддерживается только для ККТ версий 5.X, работающих по ФФД ≥ 1.2.
    """
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
    """
    Получить статус проверки сервера ИСМ.

    Вызывать до тех пор, пока check_ready не станет true.
    """
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
