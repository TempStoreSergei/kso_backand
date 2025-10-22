from pydantic import BaseModel, Field


class CashOperationRequest(BaseModel):
    """Запрос на операцию с наличными"""
    amount: float = Field(..., description="Сумма операции", gt=0)
    cashier_name: str = Field(..., description="Имя кассира")
