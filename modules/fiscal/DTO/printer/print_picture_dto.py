from typing import Optional

from pydantic import BaseModel, Field


class PrintPictureRequest(BaseModel):
    """Запрос на печать картинки из файла"""
    filename: str = Field(..., description="Путь к файлу картинки (bmp или png без прозрачности)")
    alignment: int = Field(0, description="Выравнивание: 0=влево, 1=по центру, 2=вправо")
    scale_percent: int = Field(100, description="Масштаб в процентах", ge=1, le=1000)
    left_margin: Optional[int] = Field(None, description="Дополнительный отступ слева в пикселях")


class PrintPictureByNumberRequest(BaseModel):
    """Запрос на печать картинки из памяти ККТ"""
    picture_number: int = Field(..., description="Номер картинки в памяти ККТ (отсчёт от 0)")
    alignment: int = Field(0, description="Выравнивание: 0=влево, 1=по центру, 2=вправо")
    left_margin: Optional[int] = Field(None, description="Дополнительный отступ слева в пикселях")
    defer: int = Field(0, description="Отложенная печать: 0=нет, 1=перед чеком, 2=после чека")
