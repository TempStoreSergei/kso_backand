from pydantic import BaseModel


class ResetBillCountResponseDTO(BaseModel):
    status: bool
    detail: str
