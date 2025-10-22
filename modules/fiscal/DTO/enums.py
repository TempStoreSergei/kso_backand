from enum import IntEnum


class TaxType(IntEnum):
    """Типы налогов (НДС)"""
    NONE = 0  # Без НДС
    VAT0 = 1  # НДС 0%
    VAT10 = 2  # НДС 10%
    VAT20 = 3  # НДС 20%
    VAT110 = 4  # НДС 10/110
    VAT120 = 5  # НДС 20/120


class PaymentType(IntEnum):
    """Типы оплаты"""
    CASH = 0  # Наличные
    ELECTRONICALLY = 1  # Электронными
    PREPAID = 2  # Предварительная оплата (аванс)
    CREDIT = 3  # Последующая оплата (кредит)
    OTHER = 4  # Иная форма оплаты
