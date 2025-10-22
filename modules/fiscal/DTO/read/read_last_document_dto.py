from pydantic import BaseModel, Field


class ReadLastDocumentJournalRequestDTO(BaseModel):
    """Запрос на чтение последнего закрытого документа из электронного журнала"""
    device_id: int = Field(..., description="ID устройства")
