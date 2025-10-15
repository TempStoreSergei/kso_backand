from enum import Enum

from pydantic import BaseModel, Field


class FineType(str, Enum):
    violation_rules = 'violationRules'
    damage_to_property = 'damageToProperty'


class AddFineRequestDTO(BaseModel):
    name: str
    price: int
    type: FineType


class AddFineResponseDTO(BaseModel):
    id: int
    detail: str
