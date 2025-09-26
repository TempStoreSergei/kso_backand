from pydantic import BaseModel


class StopAcceptingPaymentResponseDTO(BaseModel):
    status: bool
    detail: str | None
