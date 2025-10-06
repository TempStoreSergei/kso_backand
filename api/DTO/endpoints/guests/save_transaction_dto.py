from datetime import datetime

from pydantic import BaseModel, Field


class GuestAddTransactionRequestDTO(BaseModel):
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    surname: str | None = Field(None)


class AddTransactionRequestDTO(BaseModel):
    guest: GuestAddTransactionRequestDTO
    services: list[int]
    room_id: int = Field(alias='roomId')
    check_in: datetime | None = Field(None, alias='checkIn')
    check_out: datetime | None = Field(None, alias='checkOut')
    payment_type: str = Field(alias='paymentType')


class AddTransactionResponseDTO(BaseModel):
    transaction_id: int
    detail: str