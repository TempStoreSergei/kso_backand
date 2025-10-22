from typing import Optional

from pydantic import BaseModel, Field


class PrintBarcodeRequest(BaseModel):
    """Запрос на печать штрихкода со всеми параметрами"""
    barcode: str = Field(..., description="Данные штрихкода (до 500 символов)", max_length=500)
    barcode_type: int = Field(
        17,
        description=(
            "Тип штрихкода:\n"
            "Одномерные: 0=EAN-8, 1=EAN-13, 2=UPC-A, 3=UPC-E, 4=Code39, 5=Code93, 6=Code128, "
            "7=Codabar, 8=ITF, 9=ITF-14, 10=GS1-128, 11=Code39Extended\n"
            "Двумерные: 17=QR (LIBFPTR_BT_QR), 18=PDF417, 19=AZTEC"
        )
    )
    alignment: int = Field(0, description="Выравнивание: 0=влево, 1=по центру, 2=вправо")
    scale: int = Field(2, description="Коэффициент увеличения (1-10)", ge=1, le=10)
    left_margin: Optional[int] = Field(None, description="Дополнительный отступ слева в пикселях")
    invert: Optional[bool] = Field(None, description="Инверсия цвета")
    height: Optional[int] = Field(None, description="Высота штрихкода в пикселях (для одномерных)")
    print_text: Optional[bool] = Field(None, description="Печать данных ШК под штрихкодом (для одномерных)")
    correction: Optional[int] = Field(None, description="Коррекция: 0=по умолчанию, 1=минимум, 2-3 (QR/AZTEC), 4-8 (PDF417)")
    version: Optional[int] = Field(None, description="Версия QR-кода (1-40) или Aztec")
    columns: Optional[int] = Field(None, description="Количество столбцов PDF417")
    defer: int = Field(0, description="Отложенная печать: 0=нет, 1=перед чеком, 2=после чека")
