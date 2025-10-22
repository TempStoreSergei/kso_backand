from pydantic import BaseModel, Field
from typing import Optional


class OpenShiftRequest(BaseModel):
    """Запрос на открытие смены"""
    cashier_name: Optional[str] = Field(None, description="Имя кассира (если не указано, используется из настроек)")
    cashier_inn: Optional[str] = Field(None, description="ИНН кассира (если не указано, используется из настроек)")
