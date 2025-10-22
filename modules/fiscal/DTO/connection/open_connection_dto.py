from typing import Any

from pydantic import BaseModel, Field


class OpenConnectionRequest(BaseModel):
    """Запрос на открытие соединения"""
    settings: dict[str, Any] = Field(
        None,
        description="Настройки подключения (IPAddress, IPPort, ComFile, BaudRate и т.д.)"
    )
