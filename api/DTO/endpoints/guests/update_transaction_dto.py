from datetime import datetime

from pydantic import BaseModel, Field


class GuestUpdateTransactionRequestDTO(BaseModel):
    first_name: str | None = Field(None, alias='firstName')
    last_name: str | None = Field(None, alias='lastName')
    surname: str | None = Field(None)


class UpdateTransactionRequestDTO(BaseModel):
    guest: GuestUpdateTransactionRequestDTO | None = Field(None)
    services: list[int] | None = Field(None)
    room_id: int | None = Field(None, alias='roomId')
    check_in: datetime | None = Field(None, alias='checkIn')
    check_out: datetime | None = Field(None, alias='checkOut')


class UpdateTransactionResponseDTO(BaseModel):
    transaction_id: int
    detail: str
