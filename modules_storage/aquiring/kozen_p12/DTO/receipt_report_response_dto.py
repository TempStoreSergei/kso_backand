from pydantic import BaseModel


class ReceiptReportResponseDTO(BaseModel):
    status: bool
    detail: str | None
    data: dict | None
