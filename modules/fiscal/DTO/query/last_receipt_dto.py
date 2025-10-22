from pydantic import BaseModel, Field
from datetime import datetime


class LastReceiptQueryRequestDTO(BaseModel):
    """Запрос информации о последнем чеке из ФН"""
    pass


class LastReceiptInfoDTO(BaseModel):
    """Информация о последнем чеке"""
    document_number: int = Field(..., description="Номер документа")
    receipt_sum: float = Field(..., description="Сумма чека")
    fiscal_sign: str = Field(..., description="Фискальный признак документа")
    date_time: str = Field(..., description="Дата и время документа")
    receipt_type: int = Field(..., description="Тип чека")
    receipt_type_name: str = Field(..., description="Название типа чека")
