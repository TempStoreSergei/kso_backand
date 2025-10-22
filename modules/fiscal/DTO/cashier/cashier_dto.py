from pydantic import BaseModel, Field
from typing import Optional


class SetCashierRequest(BaseModel):
    """Запрос на установку текущего кассира"""
    cashier_name: str = Field(..., description="Имя кассира")
    cashier_inn: Optional[str] = Field(None, description="ИНН кассира")


class CashierInfoDTO(BaseModel):
    """Информация о текущем кассире"""
    cashier_name: str = Field(..., description="Имя кассира")
    cashier_inn: Optional[str] = Field(None, description="ИНН кассира")
    source: str = Field(..., description="Источник данных: 'settings' или 'dynamic'")
