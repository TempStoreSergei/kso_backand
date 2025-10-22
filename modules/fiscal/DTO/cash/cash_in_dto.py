from pydantic import BaseModel, Field


class CashOperationRequest(BaseModel):
    """Запрос на операцию с наличными"""
    amount: int = Field(..., description="Сумма операции в копейках", gt=0)
    cashier_name: str = Field(..., description="Имя кассира")
