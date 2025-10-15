from pydantic import BaseModel, Field


class UpdateServiceRequestDTO(BaseModel):
    id: int
    name: str | None = Field(None)
    price: int | None = Field(None)
    tax: int | None = Field(None)
    is_countable: bool | None = Field(None, alias='isCountable')
    is_duration: bool | None = Field(None, alias='isDuration')


class UpdateServiceResponseDTO(BaseModel):
    id: int
    detail: str
