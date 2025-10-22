from pydantic import BaseModel, Field, ConfigDict, computed_field

from modules.hotel.DTO.enums import PaymentType


class GuestGetTransactionResponseDTO(BaseModel):
    """DTO для гостя в ответе на получение транзакции."""
    id: int = Field(description="ID гостя", examples=[1])
    first_name: str = Field(
        validation_alias='first_name',
        alias='firstName',
        description="Имя гостя",
        examples=["Иван"],
    )
    last_name: str = Field(
        validation_alias='last_name',
        alias='lastName',
        description="Фамилия гостя",
        examples=["Иванов"],
    )
    surname: str | None = Field(None, description="Отчество гостя", examples=["Иванович"])

    model_config = ConfigDict(from_attributes=True)


class ServiceGetTransactionResponseDTO(BaseModel):
    """DTO для услуги в ответе на получение транзакции."""
    id: int = Field(description="ID услуги", examples=[1])
    name: str = Field(description="Название услуги", examples=["Парковка"])
    price: int = Field(description="Цена услуги", examples=[500])
    tax: int = Field(description="Налог на услугу", examples=[50])
    count: int | None = Field(None, description="Количество услуг", examples=[2])
    duration: int | None = Field(None, description="Продолжительность услуги", examples=[3])

    @computed_field(alias="totalPrice")
    @property
    def total_price(self) -> int:
        """Общая стоимость услуги."""
        if self.count:
            return self.price * self.count
        elif self.duration:
            return self.price * self.duration
        else:
            return self.price

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
    """DTO для штрафа в ответе на получение транзакции."""
    id: int = Field(description="ID штрафа", examples=[1])
    name: str = Field(description="Название штрафа", examples=["Нарушение правил"])
    price: int = Field(description="Цена штрафа", examples=[1000])
    type: str = Field(description="Тип штрафа", examples=["violationRules"])
    count: int = Field(description="Количество штрафов", examples=[1])

    @computed_field(alias="totalPrice")
    @property
    def total_price(self) -> int:
        """Общая стоимость штрафа."""
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
    """DTO для номера в ответе на получение транзакции."""
    number: str = Field(description="Номер комнаты", examples=["101"])
    type: str = Field(description="Тип номера", examples=["econom"])
    building: int = Field(description="Корпус", examples=[1])
    count_days: int | None = Field(
        None, serialization_alias='countDays', description="Количество дней", examples=[5]
    )
    price: int = Field(description="Цена за ночь", examples=[1000])
    total_price: int | None = Field(
        None, serialization_alias='totalPrice', description="Общая стоимость", examples=[5000]
    )

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class ItemGetTransactionsResponseDTO(BaseModel):
    """DTO для одной транзакции в списке."""
    id: int = Field(description="ID транзакции", examples=[1])
    guest: GuestGetTransactionResponseDTO = Field(description="Информация о госте")
    services: list[ServiceGetTransactionResponseDTO] = Field(description="Список услуг")
    fines: list[FineGetTransactionResponseDTO] = Field(description="Список штрафов")
    room: RoomGetTransactionResponseDTO = Field(description="Информация о номере")
    payment_type: PaymentType = Field(
        validation_alias='payment_type',
        serialization_alias='paymentType',
        description="Тип оплаты",
        examples=["Наличные"],
    )

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class GetTransactionsResponseDTO(BaseModel):
    """DTO для ответа на получение списка транзакций."""
    transactions: list[ItemGetTransactionsResponseDTO] = Field(description="Список транзакций")
