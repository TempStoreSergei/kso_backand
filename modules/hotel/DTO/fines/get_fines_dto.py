from pydantic import BaseModel, Field, ConfigDict

from modules.hotel.DTO.enums import FineType


class ItemGetFinesResponseDTO(BaseModel):
    """DTO для одного штрафа в списке."""
    id: int = Field(description="ID штрафа", examples=[1])
    name: str = Field(description="Название штрафа", examples=["Нарушение правил"])
    price: int = Field(description="Цена штрафа", examples=[1000])
    type: FineType = Field(description="Тип штрафа", examples=["violationRules"])

    model_config = ConfigDict(from_attributes=True)


class GetFinesResponseDTO(BaseModel):
    """DTO для ответа на получение списка штрафов."""
    fines: list[ItemGetFinesResponseDTO] = Field(description="Список штрафов")
