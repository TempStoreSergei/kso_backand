from pydantic import BaseModel, Field


class UpdateServiceRequestDTO(BaseModel):
    """DTO для обновления услуги."""
    id: int = Field(description="ID услуги", examples=[1])
    name: str | None = Field(None, description="Новое название услуги", examples=["Завтрак"])
    price: int | None = Field(None, description="Новая цена услуги", examples=[1000])
    tax: int | None = Field(None, description="Новый налог на услугу", examples=[100])
    is_countable: bool | None = Field(
        None, alias='isCountable',
        description="Новое значение, является ли услуга исчисляемой",
        examples=[False],
    )
    is_duration: bool | None = Field(
        None, alias='isDuration',
        description="Новое значение, является ли услуга услугой с продолжительностью",
        examples=[True],
    )


class UpdateServiceResponseDTO(BaseModel):
    """DTO для ответа на обновление услуги."""
    id: int = Field(description="ID обновленной услуги", examples=[1])
    detail: str = Field(description="Детали ответа", examples=["Service updated"])
