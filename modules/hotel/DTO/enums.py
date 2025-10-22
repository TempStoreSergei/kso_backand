from enum import Enum


class RoomType(str, Enum):
    """Тип номера."""
    four_bed = 'fourBed'
    six_bed = 'sixBed'
    eight_bed = 'eightBed'


class FineType(str, Enum):
    """Тип штрафа."""
    violation_rules = 'violationRules'
    damage_to_property = 'damageToProperty'


class PaymentType(str, Enum):
    """Тип оплаты."""
    cash = 'Наличные'
    electronic = 'Он-лайн платёж'
