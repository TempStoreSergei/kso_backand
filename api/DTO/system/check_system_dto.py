from pydantic import BaseModel, Field


class DeviceCheckSystemResponseDTO(BaseModel):
    connect: bool
    detail: str | None = Field(None)


class CheckSystemResponseDTO(BaseModel):
    fiscal: DeviceCheckSystemResponseDTO | None
    acquiring: DeviceCheckSystemResponseDTO | None
    scanner: DeviceCheckSystemResponseDTO | None
