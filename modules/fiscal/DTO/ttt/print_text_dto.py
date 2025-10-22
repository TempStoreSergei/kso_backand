from typing import Optional

from pydantic import BaseModel, Field


class PrintTextRequest(BaseModel):
    """Запрос на печать текста со всеми параметрами"""
    text: str = Field("", description="Строка для печати")
    alignment: int = Field(0, description="Выравнивание: 0=влево (LIBFPTR_ALIGNMENT_LEFT), 1=по центру (CENTER), 2=вправо (RIGHT)")
    wrap: int = Field(0, description="Перенос строки: 0=не переносить (LIBFPTR_TW_NONE), 1=по словам (TW_WORDS), 2=по символам (TW_CHARS)")
    font: Optional[int] = Field(None, description="Номер шрифта (зависит от модели ККТ)")
    double_width: Optional[bool] = Field(None, description="Двойная ширина шрифта")
    double_height: Optional[bool] = Field(None, description="Двойная высота шрифта")
    linespacing: Optional[int] = Field(None, description="Межстрочный интервал")
    brightness: Optional[int] = Field(None, description="Яркость печати")
    defer: int = Field(0, description="Отложенная печать: 0=нет (LIBFPTR_DEFER_NONE), 1=перед чеком (PRE), 2=после чека (POST), 3=рядом с ШК (OVERLAY)")
