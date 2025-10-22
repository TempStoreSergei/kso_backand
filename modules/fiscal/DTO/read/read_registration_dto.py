from pydantic import BaseModel, Field


class ReadRegistrationDocumentRequestDTO(BaseModel):
    """Запрос на чтение документа регистрации из ФН"""
    device_id: int = Field(..., description="ID устройства")
    registration_number: int = Field(..., description="Порядковый номер регистрации", ge=1)
