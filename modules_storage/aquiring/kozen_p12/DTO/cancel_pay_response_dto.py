from pydantic import BaseModel


class CancelPaymentResponseDTO(BaseModel):
    status: bool
    detail: str | None
    data: dict | None
