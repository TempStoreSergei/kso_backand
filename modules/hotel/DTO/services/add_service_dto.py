from pydantic import BaseModel, Field


class AddServiceRequestDTO(BaseModel):
    name: str
    price: int
    tax: int
    is_countable: bool = Field(alias='isCountable')
    is_duration: bool = Field(alias='isDuration')


class AddServiceResponseDTO(BaseModel):
    id: int
    detail: str
