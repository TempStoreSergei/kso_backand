from pydantic import BaseModel, Field


class ReadSettingsRequestDTO(BaseModel):
    """Запрос на чтение настроек ККТ"""
    device_id: int = Field(..., description="ID устройства")


class SettingDTO(BaseModel):
    """Настройка ККТ"""
    setting_id: int = Field(..., description="Номер настройки")
    setting_type: int = Field(..., description="Тип настройки (1-число, 2-bool, 3-строка)")
    setting_name: str = Field(..., description="Название настройки")
    setting_value: str | int | bool = Field(..., description="Значение настройки")
