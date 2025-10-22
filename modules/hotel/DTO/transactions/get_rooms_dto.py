from pydantic import BaseModel, Field


class GetRoomsResponseDTO(BaseModel):
    """DTO для ответа на получение списка номеров."""
    rooms1: list[str] = Field(description="Список номеров в первом корпусе", examples=[["101", "102"]])
    rooms2: list[str] = Field(description="Список номеров во втором корпусе", examples=[["201", "202"]])
    rooms3: list[str] = Field(description="Список номеров в третьем корпусе", examples=[["301", "302"]])
