from pydantic import BaseModel


class StartPaymentResponseDTO(BaseModel):
    status: bool
    detail: str | None
