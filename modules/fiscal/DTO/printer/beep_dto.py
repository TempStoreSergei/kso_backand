from pydantic import BaseModel, Field


class BeepRequest(BaseModel):
    """Запрос на звуковой сигнал"""
    frequency: int = Field(2000, description="Частота звука в Гц (100-10000)", ge=100, le=10000)
    duration: int = Field(100, description="Длительность звука в мс (10-5000)", ge=10, le=5000)
