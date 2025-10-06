from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class GuestGetTransactionResponseDTO(BaseModel):
    id: int
    first_name: str = Field(validation_alias='first_name', alias='firstName')
    last_name: str = Field(validation_alias='last_name', alias='lastName')
    surname: str | None = Field(None)

    model_config = ConfigDict(from_attributes=True)


class ServiceGetTransactionResponseDTO(BaseModel):
    id: int
    name: str
    price: int
    tax: int

    model_config = ConfigDict(from_attributes=True)


class RoomGetTransactionResponseDTO(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ItemGetTransactionsResponseDTO(BaseModel):
    id: int
    guest: GuestGetTransactionResponseDTO
    services: list[ServiceGetTransactionResponseDTO]
    room: RoomGetTransactionResponseDTO
    check_in: datetime | None = Field(None, validation_alias='check_in', alias='checkIn')
    check_out: datetime | None = Field(None, validation_alias='check_out', alias='checkOut')
    payment_type: str = Field(validation_alias='payment_type', alias='paymentType')

    model_config = ConfigDict(from_attributes=True)


class GetTransactionsResponseDTO(BaseModel):
    transactions: list[ItemGetTransactionsResponseDTO]
