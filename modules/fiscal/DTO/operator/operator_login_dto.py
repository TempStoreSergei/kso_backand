from typing import Optional

from pydantic import BaseModel, Field


class OperatorLoginRequest(BaseModel):
    """Регистрация кассира"""
    operator_name: str = Field(..., description="ФИО кассира", max_length=255)
    operator_vatin: Optional[str] = Field(None, description="ИНН кассира (12 цифр)", max_length=12)
