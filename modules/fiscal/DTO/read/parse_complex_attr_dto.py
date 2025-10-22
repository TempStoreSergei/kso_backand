from pydantic import BaseModel, Field


class ParseComplexAttributeRequestDTO(BaseModel):
    """Запрос на разбор составного реквизита"""
    device_id: int = Field(..., description="ID устройства")
    tag_value: list[int] = Field(..., description="Массив байтов со значением составного реквизита")
