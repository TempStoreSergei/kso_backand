from pydantic import BaseModel, Field


class ChangeLabelRequest(BaseModel):
    """Изменение метки драйвера для логирования"""
    label: str = Field(..., description="Метка драйвера (используется в логах с модификатором %L)", max_length=50)
