from typing import Optional

from pydantic import BaseModel, Field


class LoggingConfigRequest(BaseModel):
    """Настройка логирования драйвера"""
    root_level: str = Field("ERROR", description="Уровень логирования: ERROR, INFO, DEBUG")
    fiscal_printer_level: Optional[str] = Field(None, description="Уровень для FiscalPrinter (ERROR, INFO, DEBUG)")
    transport_level: Optional[str] = Field(None, description="Уровень для Transport (ERROR, INFO, DEBUG)")
    ethernet_over_transport_level: Optional[str] = Field(None, description="Уровень для EthernetOverTransport")
    device_debug_level: Optional[str] = Field(None, description="Уровень для DeviceDebug")
    usb_level: Optional[str] = Field(None, description="Уровень для USB")
    com_level: Optional[str] = Field(None, description="Уровень для COM")
    tcp_level: Optional[str] = Field(None, description="Уровень для TCP")
    bluetooth_level: Optional[str] = Field(None, description="Уровень для Bluetooth")
    enable_console: bool = Field(False, description="Включить вывод в консоль")
    max_days_keep: int = Field(14, description="Количество дней хранения логов", ge=1, le=365)
