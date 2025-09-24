from pydantic import BaseModel


class TestBillDispenseResponseDTO(BaseModel):
    status: bool
    detail: str
