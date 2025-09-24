from pydantic import BaseModel


class TestBillAcceptResponseDTO(BaseModel):
    status: bool
    detail: str
