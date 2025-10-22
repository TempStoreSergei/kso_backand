from pydantic import BaseModel, Field

from modules.hotel.DTO.enums import RoomType


class GuestUpdateTransactionRequestDTO(BaseModel):
    """DTO для обновления гостя в транзакции."""
    first_name: str | None = Field(
        None, alias='firstName', description="Новое имя гостя", examples=["Петр"]
    )
    last_name: str| None = Field(
        None, alias='lastName', description="Новая фамилия гостя", examples=["Петров"]
    )
    surname: str | None = Field(None, description="Новое отчество гостя", examples=["Петрович"])


class RoomUpdateTransactionRequestDTO(BaseModel):
    """DTO для обновления номера в транзакции."""
    number: str | None = Field(None, description="Новый номер комнаты", examples=["102-1"])
    type: RoomType | None = Field(None, description="Новый тип номера", examples=["fourBed"])
    building: int | None = Field(None, description="Новый корпус", examples=[2])


class UpdateTransactionRequestDTO(BaseModel):
    """DTO для обновления транзакции."""
    id: int = Field(description="ID транзакции", examples=[1])
    guest: GuestUpdateTransactionRequestDTO | None = Field(
        None, description="Новая информация о госте"
    )
    room: RoomUpdateTransactionRequestDTO | None = Field(
        None, description="Новая информация о номере"
    )


class UpdateTransactionResponseDTO(BaseModel):
    """DTO для ответа на обновление транзакции."""
    transaction_id: int = Field(description="ID обновленной транзакции", examples=[1])
    detail: str = Field(description="Детали ответа", examples=["Transaction updated"])
