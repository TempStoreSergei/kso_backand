from pydantic import BaseModel, Field

from modules.hotel.DTO.enums import FineType


class AddFineRequestDTO(BaseModel):
    """DTO для добавления штрафа."""
    name: str = Field(description="Название штрафа", examples=["Нарушение правил"])
    price: int = Field(description="Цена штрафа", examples=[1000])
    type: FineType = Field(description="Тип штрафа", examples=['violationRules'])


class AddFineResponseDTO(BaseModel):
    """DTO для ответа на добавление штрафа."""
    id: int = Field(description="ID штрафа", examples=[1])
    detail: str = Field(description="Детали ответа", examples=["Fine added"])
