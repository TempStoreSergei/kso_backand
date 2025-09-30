from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class WSEventType(str, Enum):
    get_one_item = 'GetOneItem'


class WSEventDTO(BaseModel):
    event: WSEventType
    data: Any


class WSItemDataDTO(BaseModel):
    name: str
