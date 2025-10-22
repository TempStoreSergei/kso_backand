from pydantic import BaseModel, Field
from datetime import datetime


class ReadLicensesRequestDTO(BaseModel):
    """Запрос на чтение списка лицензий"""
    pass


class LicenseDTO(BaseModel):
    """Информация о лицензии/коде защиты"""
    license_number: int = Field(..., description="Номер кода защиты / лицензии")
    license_name: str = Field(..., description="Наименование кода защиты / лицензии")
    valid_from: str = Field(..., description="Дата начала действия лицензии")
    valid_until: str = Field(..., description="Дата окончания действия лицензии")
