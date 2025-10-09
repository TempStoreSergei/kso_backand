from pydantic import BaseModel, Field


class AddServiceRequestDTO(BaseModel):
    name: str
    price: int
    tax: int


class AddServiceResponseDTO(BaseModel):
    id: int
    detail: str
