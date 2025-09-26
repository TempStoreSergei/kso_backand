from pydantic import BaseModel


class SetMaxBillCountResponseDTO(BaseModel):
    status: bool
    detail: str
