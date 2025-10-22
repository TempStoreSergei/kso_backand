from pydantic import BaseModel, Field


class ReadFnDocumentRequestDTO(BaseModel):
    """Запрос на чтение документа из ФН"""
    document_number: int = Field(..., description="Номер фискального документа для чтения", ge=1)


class TlvRecordDTO(BaseModel):
    """TLV-структура реквизита"""
    tag_number: int = Field(..., description="Номер реквизита")
    tag_name: str = Field(..., description="Название реквизита")
    tag_type: int = Field(..., description="Тип реквизита")
    tag_value: str | int | float | bool | list | None = Field(None, description="Значение реквизита")
    is_complex: bool = Field(False, description="Составной реквизит")
    is_repeatable: bool = Field(False, description="Может повторяться")


class ReadFnDocumentResponseDTO(BaseModel):
    """Ответ при чтении документа из ФН"""
    success: bool = Field(..., description="Статус операции")
    message: str | None = Field(None, description="Сообщение")
    data: dict | None = Field(None, description="Данные документа")
