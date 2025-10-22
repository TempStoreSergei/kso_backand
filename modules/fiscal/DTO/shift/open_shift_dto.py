from pydantic import BaseModel, Field


class OpenShiftRequest(BaseModel):
    """Запрос на открытие смены"""
    cashier_name: str = Field(..., description="Имя кассира")
