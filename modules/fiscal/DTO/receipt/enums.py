"""Перечисления (Enums) для работы с чеками"""
from enum import IntEnum


class ReceiptType(IntEnum):
    """
    Типы чеков (LIBFPTR_RT_*)

    Используется в параметре LIBFPTR_PARAM_RECEIPT_TYPE при открытии чека.
    """
    CLOSED = 0  # Чек закрыт (не активен)
    SELL = 1  # Чек прихода (продажа)
    SELL_RETURN = 2  # Чек возврата прихода
    BUY = 4  # Чек расхода (покупка)
    BUY_RETURN = 5  # Чек возврата расхода
    SELL_CORRECTION = 7  # Чек коррекции прихода
    SELL_RETURN_CORRECTION = 8  # Чек коррекции возврата прихода
    BUY_CORRECTION = 9  # Чек коррекции расхода
    BUY_RETURN_CORRECTION = 10  # Чек коррекции возврата расхода


class PaymentType(IntEnum):
    """
    Типы оплаты (LIBFPTR_PARAM_PAYMENT_TYPE)

    Используется при добавлении оплаты в чек.
    """
    CASH = 0  # Наличные
    ELECTRONICALLY = 1  # Безналичные (электронные)
    PREPAID = 2  # Аванс (предоплата)
    CREDIT = 3  # Кредит (постоплата)
    OTHER = 4  # Иная форма оплаты


class TaxType(IntEnum):
    """
    Типы налогообложения (НДС) (LIBFPTR_PARAM_TAX_TYPE)

    Используется при регистрации товара/услуги в чеке.
    """
    VAT_20 = 1  # НДС 20%
    VAT_10 = 2  # НДС 10%
    VAT_20_120 = 3  # НДС 20/120 (в сумме)
    VAT_10_110 = 4  # НДС 10/110 (в сумме)
    VAT_0 = 5  # НДС 0%
    NO_VAT = 6  # Без НДС


class TaxationSystem(IntEnum):
    """
    Системы налогообложения (LIBFPTR_PARAM_TAX_SYSTEM, тег 1055)

    Используется для указания применяемой системы налогообложения.
    """
    OSN = 0  # Общая (ОСН)
    USN_INCOME = 1  # Упрощенная доход (УСН доход)
    USN_INCOME_OUTCOME = 2  # Упрощенная доход минус расход (УСН доход-расход)
    ENVD = 3  # Единый налог на вмененный доход (ЕНВД)
    ESN = 4  # Единый сельскохозяйственный налог (ЕСН)
    PATENT = 5  # Патентная система налогообложения (ПСН)


class PaymentMethodType(IntEnum):
    """
    Признак способа расчета (тег 1214)

    Указывает на способ расчета между покупателем и продавцом.
    """
    FULL_PREPAYMENT = 1  # Предоплата 100%
    PARTIAL_PREPAYMENT = 2  # Частичная предоплата
    ADVANCE = 3  # Аванс
    FULL_PAYMENT = 4  # Полный расчет
    PARTIAL_PAYMENT_CREDIT = 5  # Частичный расчет и кредит
    CREDIT = 6  # Передача в кредит
    CREDIT_PAYMENT = 7  # Оплата кредита


class PaymentObjectType(IntEnum):
    """
    Признак предмета расчета (тег 1212)

    Указывает на тип продаваемой позиции.
    """
    COMMODITY = 1  # Товар
    EXCISE = 2  # Подакцизный товар
    JOB = 3  # Работа
    SERVICE = 4  # Услуга
    GAMBLING_BET = 5  # Ставка азартной игры
    GAMBLING_PRIZE = 6  # Выигрыш азартной игры
    LOTTERY_TICKET = 7  # Лотерейный билет
    LOTTERY_PRIZE = 8  # Выигрыш лотереи
    INTELLECTUAL_ACTIVITY = 9  # РИД (результаты интеллектуальной деятельности)
    PAYMENT = 10  # Платеж
    AGENT_COMMISSION = 11  # Агентское вознаграждение
    COMPOSITE = 12  # Составной предмет расчета
    ANOTHER = 13  # Иной предмет расчета
    PROPERTY_RIGHT = 14  # Имущественное право
    NON_OPERATING_INCOME = 15  # Внереализационный доход
    INSURANCE_PREMIUM = 16  # Страховые взносы
    SALES_TAX = 17  # Торговый сбор
    RESORT_FEE = 18  # Курортный сбор
    DEPOSIT = 19  # Залог
    EXPENSE = 20  # Расход
    PENSION_INSURANCE_IP = 21  # Взносы на ОПС ИП
    PENSION_INSURANCE = 22  # Взносы на ОПС
    MEDICAL_INSURANCE_IP = 23  # Взносы на ОМС ИП
    MEDICAL_INSURANCE = 24  # Взносы на ОМС
    SOCIAL_INSURANCE = 25  # Взносы на ОСС
    CASINO_PAYMENT = 26  # Платеж казино


class AgentType(IntEnum):
    """
    Признак агента (тег 1057)

    Указывает на тип агентской схемы.
    """
    BANK_PAYMENT_AGENT = 0  # Банковский платежный агент
    BANK_PAYMENT_SUBAGENT = 1  # Банковский платежный субагент
    PAYMENT_AGENT = 2  # Платежный агент
    PAYMENT_SUBAGENT = 3  # Платежный субагент
    ATTORNEY = 4  # Поверенный
    COMMISSION_AGENT = 5  # Комиссионер
    ANOTHER = 6  # Другой тип агента


class CorrectionType(IntEnum):
    """
    Тип коррекции (тег 1173)

    Указывает основание для коррекционного чека.
    """
    SELF = 0  # Самостоятельная операция
    BY_PRESCRIPTION = 1  # По предписанию налогового органа
