from pydantic import BaseModel, Field, ConfigDict, computed_field


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
    count: int | None = Field(None)
    duration: int | None = Field(None)

    @computed_field(alias="totalPrice")
    @property
    def total_price(self) -> int:
        if self.count:
            return self.price * self.count
        if self.duration:
            return self.price * self.duration

    @classmethod
    def from_row(cls, row):
        """Создаёт DTO из строки SQL результата"""
        return cls(
            id=row[0],
            name=row[1],
            price=row[2],
            tax=row[3],
            count=row[4],
            duration=row[5]
        )


class FineGetTransactionResponseDTO(BaseModel):
    id: int
    name: str
    price: int
    type: str
    count: int

    @computed_field(alias="totalPrice")
    @property
    def total_price(self) -> int:
        return self.price * self.count

    @classmethod
    def from_row(cls, row):
        """Создаёт DTO из строки SQL результата"""
        return cls(
            id=row[0],
            name=row[1],
            price=row[2],
            type=row[3],
            count=row[4]
        )


class RoomGetTransactionResponseDTO(BaseModel):
    number: str
    type: str
    building: int
    count_days: int | None = Field(None, serialization_alias='countDays')
    price: int
    total_price: int | None = Field(None, serialization_alias='totalPrice')

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class ItemGetTransactionsResponseDTO(BaseModel):
    id: int
    guest: GuestGetTransactionResponseDTO
    services: list[ServiceGetTransactionResponseDTO]
    fines: list[FineGetTransactionResponseDTO]
    room: RoomGetTransactionResponseDTO
    payment_type: str = Field(validation_alias='payment_type', serialization_alias='paymentType')

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class GetTransactionsResponseDTO(BaseModel):
    transactions: list[ItemGetTransactionsResponseDTO]
