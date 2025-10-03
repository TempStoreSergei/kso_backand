from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class WSEventType(str, Enum):
    get_one_item = 'getOneItem'
    error_payment = 'errorPayment'


class WSEventDTO(BaseModel):
    event: WSEventType
    data: Any


class WSItemDataDTO(BaseModel):
    name: str
