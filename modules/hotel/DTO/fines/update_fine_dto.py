from pydantic import BaseModel, Field

from modules.hotel.DTO.enums import FineType


class UpdateFineRequestDTO(BaseModel):
    """DTO для обновления штрафа."""
    id: int = Field(description="ID штрафа", examples=[1])
    name: str | None = Field(
        None, description="Новое название штрафа", examples=["Нарушение тишины"]
    )
    price: int | None = Field(
        None, description="Новая цена штрафа", examples=[1500]
    )
    type: FineType | None = Field(
        None, description="Новый тип штрафа", examples=['damageToProperty']
    )


class UpdateFineResponseDTO(BaseModel):
    """DTO для ответа на обновление штрафа."""
    id: int = Field(description="ID обновленного штрафа", examples=[1])
    detail: str = Field(description="Детали ответа", examples=["Fine updated"])
