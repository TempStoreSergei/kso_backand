from pydantic import BaseModel, Field


class SendScannedCodeRequestDTO(BaseModel):
    scanned_code: str


class SendScannedCodeResponseDTO(BaseModel):
    detail: str
