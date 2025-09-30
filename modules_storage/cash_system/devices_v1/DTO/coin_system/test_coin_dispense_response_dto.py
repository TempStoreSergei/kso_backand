from pydantic import BaseModel


class TestCoinDispenseResponseDTO(BaseModel):
    status: bool
    detail: str
