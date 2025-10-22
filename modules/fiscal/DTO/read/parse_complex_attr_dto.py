from pydantic import BaseModel, Field


class ParseComplexAttributeRequestDTO(BaseModel):
    """Запрос на разбор составного реквизита"""
    tag_value: list[int] = Field(..., description="Массив байтов со значением составного реквизита")
