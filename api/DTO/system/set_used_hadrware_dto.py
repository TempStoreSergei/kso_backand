from enum import Enum

from pydantic import BaseModel


class DevicesList(str, Enum):
    fiscal = 'fiscal'
    scanner = 'scanner'
    cash_system = 'cashSystem'
    acquiring = 'acquiring'


class SetUsedHardwareRequestDTO(BaseModel):
    devices: list[DevicesList]


class SetUsedHardwareResponseDTO(BaseModel):
    detail: str
