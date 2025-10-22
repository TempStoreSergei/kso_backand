from typing import Optional, List

from pydantic import BaseModel, Field


# ========== КОНСТАНТЫ ==========

# Типы чеков (LIBFPTR_PARAM_RECEIPT_TYPE)
RECEIPT_TYPE_SELL = 0  # Чек прихода (продажи)
RECEIPT_TYPE_SELL_RETURN = 1  # Чек возврата прихода
RECEIPT_TYPE_SELL_CORRECTION = 2  # Чек коррекции прихода
RECEIPT_TYPE_SELL_RETURN_CORRECTION = 3  # Чек коррекции возврата прихода
RECEIPT_TYPE_BUY = 4  # Чек расхода (покупки)
RECEIPT_TYPE_BUY_RETURN = 5  # Чек возврата расхода
RECEIPT_TYPE_BUY_CORRECTION = 6  # Чек коррекции расхода
RECEIPT_TYPE_BUY_RETURN_CORRECTION = 7  # Чек коррекции возврата расхода

# Типы налогов (LIBFPTR_PARAM_TAX_TYPE)
TAX_VAT0 = 1  # НДС 0%
TAX_VAT10 = 2  # НДС 10%
TAX_VAT20 = 3  # НДС 20%
TAX_VAT110 = 4  # НДС рассчитанный 10/110
TAX_VAT120 = 5  # НДС рассчитанный 20/120
TAX_NO = 6  # Не облагается
TAX_VAT5 = 7  # НДС 5%
TAX_VAT105 = 8  # НДС рассчитанный 5/105
TAX_VAT7 = 9  # НДС 7%
TAX_VAT107 = 10  # НДС рассчитанный 7/107

# Способы расчета (LIBFPTR_PARAM_PAYMENT_TYPE)
PAYMENT_TYPE_CASH = 0  # Наличными
PAYMENT_TYPE_ELECTRONICALLY = 1  # Безналичными
PAYMENT_TYPE_PREPAID = 2  # Предварительная оплата (аванс)
PAYMENT_TYPE_CREDIT = 3  # Последующая оплата (кредит)
PAYMENT_TYPE_OTHER = 4  # Иная форма оплаты
PAYMENT_TYPE_6 = 5  # Способ расчета №6
PAYMENT_TYPE_7 = 6  # Способ расчета №7
PAYMENT_TYPE_8 = 7  # Способ расчета №8
PAYMENT_TYPE_9 = 8  # Способ расчета №9
PAYMENT_TYPE_10 = 9  # Способ расчета №10

# Системы налогообложения (тег 1055)
TAX_SYSTEM_OSN = 0  # Общая
TAX_SYSTEM_USN_INCOME = 1  # Упрощенная доход
TAX_SYSTEM_USN_INCOME_OUTCOME = 2  # Упрощенная доход минус расход
TAX_SYSTEM_ESN = 3  # Единый сельскохозяйственный доход
TAX_SYSTEM_PATENT = 4  # Патентная система налогообложения

# Типы агентов (тег 1057)
AGENT_TYPE_BANK_PAYING_AGENT = 0  # Банковский платежный агент
AGENT_TYPE_BANK_PAYING_SUBAGENT = 1  # Банковский платежный субагент
AGENT_TYPE_PAYING_AGENT = 2  # Платежный агент
AGENT_TYPE_PAYING_SUBAGENT = 3  # Платежный субагент
AGENT_TYPE_ATTORNEY = 4  # Поверенный
AGENT_TYPE_COMMISSION_AGENT = 5  # Комиссионер
AGENT_TYPE_ANOTHER = 6  # Другой тип агента

# Типы кодов маркировки (LIBFPTR_PARAM_MARKING_CODE_TYPE для ФФД 1.2)
MARKING_CODE_TYPE_AUTO = 0  # Определить автоматически
MARKING_CODE_TYPE_UNKNOWN = 1  # Неопознанный КМ
MARKING_CODE_TYPE_SHORT = 2  # Короткий КМ
MARKING_CODE_TYPE_88_CHECK = 3  # КМ 88 символов с проверкой в ФН
MARKING_CODE_TYPE_44_NO_CHECK = 4  # КМ 44 символа без проверки в ФН
MARKING_CODE_TYPE_44_CHECK = 5  # КМ 44 символа с проверкой в ФН
MARKING_CODE_TYPE_4_NO_CHECK = 6  # КМ 4 символа без проверки в ФН

# Статусы маркированных товаров (тег 2003, 2110)
MARKING_STATUS_PIECE_SOLD = 1  # Штучный товар, реализован
MARKING_STATUS_DRY_FOR_SALE = 2  # Мерный товар, в стадии реализации
MARKING_STATUS_PIECE_RETURN = 3  # Штучный товар, возвращен
MARKING_STATUS_DRY_RETURN = 4  # Часть товара, возвращена
MARKING_STATUS_PIECE_FOR_SALE = 5  # Штучный товар, в стадии реализации
MARKING_STATUS_DRY_SOLD = 6  # Мерный товар, реализован
MARKING_STATUS_UNCHANGED = 7  # Статус товара не изменился

# Единицы измерения (тег 2108)
MEASUREMENT_UNIT_PIECE = 0  # Штука
MEASUREMENT_UNIT_GRAM = 10  # Грамм
MEASUREMENT_UNIT_KILOGRAM = 11  # Килограмм
MEASUREMENT_UNIT_TON = 12  # Тонна
MEASUREMENT_UNIT_CENTIMETER = 20  # Сантиметр
MEASUREMENT_UNIT_METER = 21  # Метр
MEASUREMENT_UNIT_SQUARE_METER = 30  # Квадратный метр
MEASUREMENT_UNIT_LITER = 51  # Литр
MEASUREMENT_UNIT_CUBIC_METER = 70  # Кубический метр


class CancelReceiptRequest(BaseModel):
    """Запрос на отмену чека"""
    clear_marking_table: bool = Field(True, description="Очистить внутреннюю таблицу КМ драйвера")


class RegistrationRequest(BaseModel):
    """Запрос на регистрацию позиции в чеке"""
    # Обязательные параметры
    name: str = Field(..., description="Наименование товара (LIBFPTR_PARAM_COMMODITY_NAME)")
    price: float = Field(..., description="Цена за единицу (LIBFPTR_PARAM_PRICE)")
    quantity: float = Field(1.0, description="Количество (LIBFPTR_PARAM_QUANTITY)")

    # Налогообложение
    tax_type: int = Field(TAX_NO, description="Тип НДС (LIBFPTR_PARAM_TAX_TYPE, 1-10)")
    tax_sum: Optional[float] = Field(None, description="Сумма налога (LIBFPTR_PARAM_TAX_SUM)")
    use_only_tax_type: bool = Field(False, description="Регистрировать только ставку налога без суммы")
    tax_mode: Optional[int] = Field(None, description="Способ начисления налога: 0=на позицию, 1=на единицу")

    # Дополнительные параметры позиции
    position_sum: Optional[float] = Field(None, description="Полная сумма позиции с учетом скидки/надбавки")
    department: Optional[int] = Field(None, description="Номер отдела (LIBFPTR_PARAM_DEPARTMENT)")
    info_discount_sum: Optional[float] = Field(None, description="Информация о скидке/надбавке")
    piece: bool = Field(False, description="Штучный товар (не печатать нули в дробной части)")
    check_sum: bool = Field(False, description="Проверять наличность в ДЯ при регистрации")

    # Фискальные реквизиты (ФФД)
    additional_attribute: Optional[str] = Field(None, description="Дополнительный реквизит предмета расчета (тег 1191)")
    measurement_unit_name: Optional[str] = Field(None, description="Единицы измерения предмета расчета (тег 1197, ФФД ≤ 1.1)")
    measurement_unit: Optional[int] = Field(None, description="Мера количества предмета расчета (тег 2108, ФФД ≥ 1.2)")
    payment_method_type: int = Field(4, description="Признак способа расчета (тег 1214)")
    payment_object_type: int = Field(1, description="Признак предмета расчета (тег 1212)")
    excise: Optional[float] = Field(None, description="Акциз (тег 1229)")
    country_code: Optional[str] = Field(None, description="Код страны происхождения товара (тег 1230)")
    customs_declaration: Optional[str] = Field(None, description="Номер таможенной декларации (тег 1231)")

    # Агенты и поставщики
    agent_type: Optional[int] = Field(None, description="Признак агента по предмету расчета (тег 1222)")
    agent_info: Optional[bytes] = Field(None, description="Данные агента (тег 1223)")
    supplier_info: Optional[bytes] = Field(None, description="Данные поставщика (тег 1224)")
    supplier_inn: Optional[str] = Field(None, description="ИНН поставщика (тег 1226)")

    # Коды товара (тег 1162 для ФФД ≤ 1.1)
    commodity_code: Optional[bytes] = Field(None, description="Код товара (тег 1162, ФФД ≤ 1.1)")

    # Коды товара (тег 1163 для ФФД ≥ 1.2) - автоопределение типа
    product_codes: Optional[List[str]] = Field(None, description="Коды товара без указания типа (LIBFPTR_PARAM_PRODUCT_CODE)")

    # Коды товара с указанием типа (теги 1300-1325)
    product_code_unknown: Optional[str] = Field(None, description="Нераспознанный код товара (тег 1300)")
    product_code_ean8: Optional[str] = Field(None, description="КТ EAN-8 (тег 1301)")
    product_code_ean13: Optional[str] = Field(None, description="КТ EAN-13 (тег 1302)")
    product_code_itf14: Optional[str] = Field(None, description="КТ ITF-14 (тег 1303)")
    product_code_gs10: Optional[str] = Field(None, description="КТ GS1.0 (тег 1304)")
    product_code_gs1m: Optional[str] = Field(None, description="КТ GS1.M (тег 1305)")
    product_code_short: Optional[str] = Field(None, description="КТ КМК короткий (тег 1306)")
    product_code_furs: Optional[str] = Field(None, description="КТ МИ меховые изделия (тег 1307)")
    product_code_egais20: Optional[str] = Field(None, description="КТ ЕГАИС-2.0 (тег 1308)")
    product_code_egais30: Optional[str] = Field(None, description="КТ ЕГАИС-3.0 (тег 1309)")

    # Маркировка (ФФД < 1.2)
    marking_code: Optional[str] = Field(None, description="Код маркировки (LIBFPTR_PARAM_MARKING_CODE)")
    marking_code_type: Optional[int] = Field(None, description="Тип кода маркировки: 0=ЕГАИС 2.0, 1=ЕГАИС 3.0, 2=другая")

    # Маркировка (ФФД ≥ 1.2)
    marking_code_ffd12: Optional[str] = Field(None, description="Код маркировки для ФФД 1.2 (тег 2000)")
    marking_code_status: Optional[int] = Field(None, description="Присвоенный статус товара (тег 2110)")
    marking_processing_mode: Optional[int] = Field(None, description="Режим обработки КМ (тег 2102)")
    marking_code_online_validation_result: Optional[int] = Field(None, description="Результат проверки сведений о товаре (тег 2106)")
    marking_product_id: Optional[str] = Field(None, description="Идентификатор товара (тег 2101)")
    marking_fractional_quantity: Optional[str] = Field(None, description="Дробное количество маркированного товара (формат '1/2')")

    # Отраслевой реквизит (тег 1260, ФФД ≥ 1.2)
    industry_attribute: Optional[bytes] = Field(None, description="Отраслевой реквизит предмета расчета (тег 1260)")


class PaymentRequest(BaseModel):
    """Запрос на регистрацию оплаты"""
    payment_type: int = Field(..., description="Способ расчета (0-9, см. PAYMENT_TYPE_*)")
    sum: float = Field(..., description="Сумма расчета (LIBFPTR_PARAM_PAYMENT_SUM)")

    # Сведения об оплате безналичными (тег 1235)
    electronically_payment_method: Optional[int] = Field(None, description="Признак способа оплаты безналичными (тег 1236)")
    electronically_id: Optional[str] = Field(None, description="Идентификатор безналичной оплаты (тег 1237)")
    electronically_add_info: Optional[str] = Field(None, description="Дополнительные сведения о безналичной оплате (тег 1238)")


class ReceiptTaxRequest(BaseModel):
    """Запрос на регистрацию налога на чек"""
    tax_type: int = Field(..., description="Тип налога (1-10, см. TAX_*)")
    tax_sum: float = Field(..., description="Сумма налога (LIBFPTR_PARAM_TAX_SUM)")


class ReceiptTotalRequest(BaseModel):
    """Запрос на регистрацию итога чека"""
    sum: float = Field(..., description="Сумма чека (LIBFPTR_PARAM_SUM)")


class CloseReceiptRequest(BaseModel):
    """Запрос на закрытие чека"""
    payment_type: Optional[int] = Field(None, description="Способ автооплаты неоплаченного остатка (по умолчанию 0=наличные)")


class WriteSalesNoticeRequest(BaseModel):
    """Запрос на передачу данных уведомления о реализации маркированного товара"""
    customer_inn: Optional[str] = Field(None, description="ИНН клиента (тег 1228)")
    industry_attributes: Optional[List[bytes]] = Field(None, description="Отраслевые реквизиты чека (тег 1261, можно несколько)")
    time_zone: Optional[int] = Field(None, description="Часовая зона (тег 1011)")


class BeginMarkingCodeValidationRequest(BaseModel):
    """Запрос на начало проверки кода маркировки"""
    marking_code: str = Field(..., description="Код маркировки (тег 2000)")
    marking_code_type: int = Field(MARKING_CODE_TYPE_AUTO, description="Тип КМ (тег 2100, 0-6)")
    marking_code_status: int = Field(..., description="Планируемый статус КМ (тег 2003, 1-7)")
    quantity: Optional[float] = Field(None, description="Количество товара (тег 1023)")
    measurement_unit: Optional[int] = Field(None, description="Мера количества товара (тег 2108)")
    marking_processing_mode: int = Field(0, description="Режим обработки кода товара (тег 2102)")
    marking_fractional_quantity: Optional[str] = Field(None, description="Дробное количество товара (тег 1292, формат '1/2')")
    timeout: int = Field(0, description="Таймаут ожидания проверки в мс (0=асинхронный режим)")
    not_send_to_server: bool = Field(False, description="Не отправлять запрос на сервер")
    not_form_request: bool = Field(False, description="Не формировать запрос")
