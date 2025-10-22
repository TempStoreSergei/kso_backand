from pydantic import BaseModel


class BaseResponseDTO(BaseModel):
    """Статус подключения"""
    success: bool
    message: str | None = None
    data: dict | None = None
