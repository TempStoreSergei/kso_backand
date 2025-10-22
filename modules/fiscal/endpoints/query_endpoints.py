from fastapi import Depends, Query
from redis.asyncio import Redis

from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO


async def get_status(
    device_id: str = Query("default", description="Идентификатор фискального регистратора"),
    redis: Redis = Depends(get_redis)
):
    """
    Запрос полной информации и статуса ККТ.

    Возвращает: модель, серийный номер, состояние смены, крышка, наличие бумаги,
    заводской номер, версию ПО, оператор, фискальные флаги и многое другое.
    """
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
    """
    Короткий запрос статуса ККТ.

    Возвращает только: денежный ящик открыт, наличие бумаги, бумага заканчивается, крышка открыта.
    """
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
    """Запрос суммы наличных в денежном ящике."""
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
    """
    Запрос состояния смены.

    Возвращает: состояние смены (закрыта/открыта/истекла), номер смены, дата и время истечения.
    """
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
    """
    Запрос состояния чека.

    Возвращает: тип чека, сумму чека, номер чека, номер документа, неоплаченный остаток, сдачу.
    """
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
    """Запрос текущих даты и времени в ККТ."""
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
    """Запрос заводского номера ККТ."""
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
    """
    Запрос информации о модели ККТ.

    Возвращает: номер модели, название модели, версию ПО.
    """
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
    """
    Запрос ширины чековой ленты.

    Возвращает ширину в символах и пикселях.
    """
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
    """
    Запрос версии модуля ККТ.

    Типы модулей:
    - 0 (LIBFPTR_UT_FIRMWARE): Прошивка
    - 1 (LIBFPTR_UT_CONFIGURATION): Конфигурация (также возвращает версию релиза)
    - 2 (LIBFPTR_UT_TEMPLATES): Движок шаблонов
    - 3 (LIBFPTR_UT_CONTROL_UNIT): Блок управления
    - 4 (LIBFPTR_UT_BOOT): Загрузчик
    """
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
    """
    Запрос суммы платежей за смену по типу оплаты и типу чека.

    Типы оплаты (LIBFPTR_PARAM_PAYMENT_TYPE):
    - 0 = наличные (CASH)
    - 1 = безналичные (ELECTRONICALLY)
    - 2 = аванс (PREPAID)
    - 3 = кредит (CREDIT)
    - 4 = иное (OTHER)

    Типы чека (LIBFPTR_PARAM_RECEIPT_TYPE):
    - 0 = продажа (SELL)
    - 1 = возврат продажи (SELL_RETURN)
    - 2 = покупка (BUY)
    - 3 = возврат покупки (BUY_RETURN)
    """
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
    """Запрос суммы внесений за смену."""
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
    """Запрос суммы выплат за смену."""
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
    """
    Запрос количества чеков за смену по типу.

    Типы чека (LIBFPTR_PARAM_RECEIPT_TYPE):
    - 0 = продажа (SELL)
    - 1 = возврат продажи (SELL_RETURN)
    - 2 = покупка (BUY)
    - 3 = возврат покупки (BUY_RETURN)
    - 4 = коррекция продажи (SELL_CORRECTION)
    - 5 = коррекция покупки (BUY_CORRECTION)
    """
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
    """
    Запрос необнуляемой суммы по типу чека.

    Необнуляемая сумма - это накопительный итог с момента фискализации ККТ.
    """
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
    """
    Запрос состояния источника питания.

    Типы источников (LIBFPTR_PARAM_POWER_SOURCE_TYPE):
    - 0 (LIBFPTR_PST_POWER_SUPPLY): Внешний блок питания
    - 1 (LIBFPTR_PST_RTC_BATTERY): Батарея часов
    - 2 (LIBFPTR_PST_BATTERY): Встроенные аккумуляторы (по умолчанию)

    Возвращает: заряд аккумулятора (%), напряжение (В), работа от аккумулятора,
    идет зарядка, может ли печатать при текущем заряде.
    """
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
    """
    Запрос температуры термопечатающей головки (ТПГ).

    Возвращает температуру в градусах Цельсия.
    """
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
    """
    Запрос фатальных ошибок ККТ.

    Возвращает флаги критических ошибок:
    - Отсутствие серийного номера
    - Сбой часов (RTC)
    - Сбой настроек
    - Сбой счетчиков
    - Сбой пользовательской памяти
    - Сбой сервисных регистров
    - Сбой реквизитов
    - Фатальная ошибка ФН
    - Установлен ФН из другой ККТ
    - Фатальная аппаратная ошибка
    - Ошибка диспетчера памяти
    - Шаблоны повреждены
    - Требуется перезагрузка
    - Ошибка универсальных счётчиков
    - Ошибка таблицы товаров
    """
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
    """Запрос MAC-адреса Ethernet."""
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
    """
    Запрос текущей конфигурации Ethernet.

    Возвращает: IP-адрес, маска сети, шлюз, DNS, порт, таймаут, DHCP, статический DNS.

    Поддерживается только для ККТ версий 5.X.
    """
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
    """
    Запрос текущей конфигурации Wi-Fi.

    Возвращает: IP-адрес, маска сети, шлюз, порт, таймаут, DHCP.

    Поддерживается только для ККТ версий 5.X.
    """
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
    """
    Запрос информации о последнем чеке из ФН.

    Возвращает информацию о последнем пробитом чеке в удобном для чтения формате:
    - Номер фискального документа
    - Сумма чека
    - Фискальный признак документа (ФПД)
    - Дата и время документа
    - Тип чека (прихода, возврата, коррекции и т.д.)

    Поддерживается для всех ККТ.
    """
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
    """
    Запрос регистрационных данных ККТ из ФН.

    Возвращает полную информацию о регистрации ККТ в удобном для чтения формате:
    - ИНН и наименование организации
    - Регистрационный номер ККТ
    - Адреса расчетов и email
    - Системы налогообложения (расшифрованные)
    - Версия ФФД (расшифрованная)
    - Признаки работы ККТ (автоматический режим, интернет, услуги и т.д.)
    - Информация об ОФД
    - Признак агента (расшифрованный)

    Поддерживается для всех ККТ.
    """
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
    """
    Запрос информации о фискальном накопителе (ФН).

    Возвращает подробную информацию о ФН в удобном для чтения формате:
    - Серийный номер ФН
    - Версия ФН
    - Тип ФН (боевая/отладочная)
    - Состояние ФН (фискальный режим, архив закрыт и т.д.)
    - Флаги ФН (смена открыта, текущая смена больше 24ч, закончена передача ФД и т.д.)
    - Критические ошибки ФН (переполнение, ошибка критических данных, несовпадение ИНН)

    Поддерживается для всех ККТ.
    """
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
    """
    Запрос статуса обмена с ОФД.

    Возвращает информацию о состоянии обмена с оператором фискальных данных:
    - Статус обмена (расшифрованные флаги: ожидает ответа, есть ответ, есть команда,
      ожидается подтверждение и т.д.)
    - Количество неотправленных документов
    - Номер первого неотправленного документа
    - Дата первого неотправленного документа

    Поддерживается для всех ККТ.
    """
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
    """
    Запрос информации о смене из ФН.

    Возвращает информацию о текущей смене:
    - Количество чеков в текущей смене (всех типов)
    - Номер текущей смены

    Поддерживается для всех ККТ.
    """
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
    """
    Запрос информации о последнем фискальном документе из ФН.

    Возвращает базовую информацию о последнем закрытом фискальном документе:
    - Номер последнего документа
    - Фискальный признак документа (ФПД)
    - Дата и время документа

    Поддерживается для всех ККТ.
    """
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
    """
    Запрос срока действия ФН.

    Возвращает информацию о сроке службы фискального накопителя:
    - Дата окончания срока действия ФН
    - Количество оставшихся регистраций
    - Количество оставшихся перерегистраций

    Поддерживается для всех ККТ.
    """
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
