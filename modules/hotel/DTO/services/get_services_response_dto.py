from pydantic import BaseModel, ConfigDict, Field


class ItemGetServicesResponseDTO(BaseModel):
    id: int
    name: str
    price: int
    tax: int
    is_countable: bool = Field(serialization_alias='isCountable')
    is_duration: bool = Field(serialization_alias='isDuration')

    model_config = ConfigDict(from_attributes=True)


class GetServicesResponseDTO(BaseModel):
    services: list[ItemGetServicesResponseDTO]
