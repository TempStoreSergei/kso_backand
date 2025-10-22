from pydantic import BaseModel, Field


class PrintFeedRequest(BaseModel):
    """Запрос на промотку ленты"""
    lines: int = Field(1, description="Количество пустых строк для промотки", ge=1, le=100)
