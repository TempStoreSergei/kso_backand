from pydantic import BaseModel


class CashCollectionResponseDTO(BaseModel):
    status: bool
    detail: str
