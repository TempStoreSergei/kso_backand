from pydantic import BaseModel


class RefundPaymentResponseDTO(BaseModel):
    status: bool
    detail: str | None
    data: dict | None
