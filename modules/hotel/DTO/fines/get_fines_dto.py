from pydantic import BaseModel, Field, ConfigDict


class ItemGetFinesResponseDTO(BaseModel):
    id: int
    name: str
    price: int
    type: str

    model_config = ConfigDict(from_attributes=True)


class GetFinesResponseDTO(BaseModel):
    fines: list[ItemGetFinesResponseDTO]
