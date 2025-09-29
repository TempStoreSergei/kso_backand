from pydantic import BaseModel


class TestCoinAcceptResponseDTO(BaseModel):
    status: bool
    detail: str
