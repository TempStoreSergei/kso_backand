from pydantic import BaseModel


class StartAcceptingPaymentResponseDTO(BaseModel):
    status: bool
    detail: str | None
