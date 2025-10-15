from pydantic import BaseModel, Field

from modules.hotel.DTO.transactions.save_transaction_dto import RoomType


class GuestUpdateTransactionRequestDTO(BaseModel):
    first_name: str | None = Field(None, alias='firstName')
    last_name: str| None = Field(None, alias='lastName')
    surname: str | None = Field(None)


class RoomUpdateTransactionRequestDTO(BaseModel):
    number: str | None = Field(None)
    type: RoomType | None = Field(None)
    building: int | None = Field(None)


class UpdateTransactionRequestDTO(BaseModel):
    id: int
    guest: GuestUpdateTransactionRequestDTO | None = Field(None)
    room: RoomUpdateTransactionRequestDTO | None = Field(None)


class UpdateTransactionResponseDTO(BaseModel):
    transaction_id: int
    detail: str
