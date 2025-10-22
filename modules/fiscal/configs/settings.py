"""
Настройки фискального модуля
"""
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings


class FiscalSettings(BaseSettings):
    """Настройки фискального модуля"""

    # Кассир по умолчанию
    cashier_name: str = "Кассир"
    cashier_inn: str = ""

    # Компания
    company_inn: str = ""
    company_payment_address: str = ""
    company_email: str = ""

    # АТОЛ Драйвер (для очереди)
    atol_driver_path: str = ""
    atol_connection_type: str = "tcp"
    atol_host: str = "localhost"
    atol_port: int = 5555
    atol_serial_port: str = ""
    atol_baudrate: int = 115200

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379

    # Пути
    log_dir: Path = Path("logs")
    receipts_dir: Path = Path("data/receipts")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


# Глобальный экземпляр настроек
fiscal_settings = FiscalSettings()
