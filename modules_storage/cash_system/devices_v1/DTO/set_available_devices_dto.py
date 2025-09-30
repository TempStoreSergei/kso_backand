from pydantic import BaseModel, Field


class SetAvailableDevicesRequestDTO(BaseModel):
    bill_acceptor: bool = Field(alias='billAcceptor')
    bill_dispenser: bool = Field(alias='billDispenser')
    coin_acceptor: bool = Field(alias='coinAcceptor')


class SetAvailableDevicesResponseDTO(BaseModel):
    detail: str
