from pydantic import BaseModel, Field


class AddBillCountRequestDTO(BaseModel):
    upper_count: int = Field(alias='upperCount')
    lower_count: int = Field(alias='lowerCount')


class AddBillCountResponseDTO(BaseModel):
    status: bool
    detail: str
