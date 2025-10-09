from pydantic import BaseModel


class TgBotNotificationsRequestDTO(BaseModel):
    token: str
    chat: str


class TgBotNotificationsResponseDTO(BaseModel):
    detail: str
