from pydantic import BaseModel, ConfigDict, Field


class ItemGetServicesResponseDTO(BaseModel):
    """DTO для одной услуги в списке."""
    id: int = Field(description="ID услуги", examples=[1])
    name: str = Field(description="Название услуги", examples=["Парковка"])
    price: int = Field(description="Цена услуги", examples=[500])
    tax: int = Field(description="Налог на услугу", examples=[50])
    is_countable: bool = Field(
        serialization_alias='isCountable',
        description="Является ли услуга исчисляемой",
        examples=[True],
    )
    is_duration: bool = Field(
        serialization_alias='isDuration',
        description="Является ли услуга услугой с продолжительностью",
        examples=[False],
    )

    model_config = ConfigDict(from_attributes=True)


class GetServicesResponseDTO(BaseModel):
    """DTO для ответа на получение списка услуг."""
    services: list[ItemGetServicesResponseDTO] = Field(description="Список услуг")
