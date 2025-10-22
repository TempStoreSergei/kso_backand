from pydantic import BaseModel, Field, model_validator

from modules.hotel.DTO.enums import RoomType, PaymentType


class GuestAddTransactionRequestDTO(BaseModel):
    """DTO для добавления гостя в транзакцию."""
    first_name: str = Field(alias='firstName', description="Имя гостя", examples=["Иван"])
    last_name: str = Field(alias='lastName', description="Фамилия гостя", examples=["Иванов"])
    surname: str | None = Field(None, description="Отчество гостя", examples=["Иванович"])


class ServiceAddTransactionRequestDTO(BaseModel):
    """DTO для добавления услуги в транзакцию."""
    id: int = Field(description="ID услуги", examples=[1])
    count: int | None = Field(None, description="Количество услуг", examples=[2])
    duration: int | None = Field(None, description="Продолжительность услуги", examples=[3])


class FineAddTransactionRequestDTO(BaseModel):
    """DTO для добавления штрафа в транзакцию."""
    id: int = Field(description="ID штрафа", examples=[1])
    count: int = Field(1, description="Количество штрафов", examples=[1])


class RoomAddTransactionRequestDTO(BaseModel):
    """DTO для добавления номера в транзакцию."""
    number: str = Field(description="Номер комнаты", examples=["101"])
    type: RoomType = Field(description="Тип номера", examples=["fourBed"])
    building: int = Field(description="Корпус", examples=[1])
    count_days: int | None = Field(
        None, alias='countDays', description="Количество дней", examples=[5]
    )


class AddTransactionRequestDTO(BaseModel):
    """DTO для добавления транзакции."""
    guest: GuestAddTransactionRequestDTO = Field(description="Информация о госте")
    services: list[ServiceAddTransactionRequestDTO] | None = Field(None, description="Список услуг")
    fines: list[FineAddTransactionRequestDTO] | None = Field(None, description="Список штрафов")
    room: RoomAddTransactionRequestDTO = Field(description="Информация о номере")
    payment_summ: int = Field(alias='paymentSumm', description="Сумма оплаты", examples=[5000])
    payment_type: PaymentType = Field(
        alias='paymentType', description="Тип оплаты", examples=["Наличные"]
    )

    @model_validator(mode='after')
    def check_services_or_fines(self):
        """Разрешено только одно из полей: services или fines"""
        has_services = bool(self.services)
        has_fines = bool(self.fines)
        if has_services and has_fines:
            raise ValueError("Должно быть заполнено только одно из полей: services или fines")
        return self


class AddTransactionResponseDTO(BaseModel):
    """DTO для ответа на добавление транзакции."""
    transaction_id: int = Field(description="ID транзакции", examples=[1])
    detail: str = Field(description="Детали ответа", examples=["Transaction added"])
