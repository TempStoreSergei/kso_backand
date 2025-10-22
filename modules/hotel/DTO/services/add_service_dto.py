from pydantic import BaseModel, Field


class AddServiceRequestDTO(BaseModel):
    """DTO для добавления услуги."""
    name: str = Field(description="Название услуги", examples=["Парковка"])
    price: int = Field(description="Цена услуги", examples=[500])
    tax: int = Field(description="Налог на услугу", examples=[50])
    is_countable: bool = Field(
        alias='isCountable', description="Является ли услуга исчисляемой", examples=[True]
    )
    is_duration: bool = Field(
        alias='isDuration',
        description="Является ли услуга услугой с продолжительностью",
        examples=[False],
    )


class AddServiceResponseDTO(BaseModel):
    """DTO для ответа на добавление услуги."""
    id: int = Field(description="ID услуги", examples=[1])
    detail: str = Field(description="Детали ответа", examples=["Service added"])
