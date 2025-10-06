from pydantic import BaseModel, ConfigDict


class ItemGetServicesResponseDTO(BaseModel):
    id: int
    name: str
    price: int
    tax: int

    model_config = ConfigDict(from_attributes=True)


class GetServicesResponseDTO(BaseModel):
    services: list[ItemGetServicesResponseDTO]
