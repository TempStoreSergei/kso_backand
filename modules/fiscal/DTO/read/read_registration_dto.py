from pydantic import BaseModel, Field


class ReadRegistrationDocumentRequestDTO(BaseModel):
    """Запрос на чтение документа регистрации из ФН"""
    registration_number: int = Field(..., description="Порядковый номер регистрации", ge=1)
