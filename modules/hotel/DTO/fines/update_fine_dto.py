from pydantic import BaseModel, Field


class UpdateFineRequestDTO(BaseModel):
    id: int
    name: str | None = Field(None)
    price: int | None = Field(None)
    type: int | None = Field(None)


class UpdateFineResponseDTO(BaseModel):
    id: int
    detail: str
