from enum import Enum


from pydantic import BaseModel, Field, model_validator


class GuestAddTransactionRequestDTO(BaseModel):
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    surname: str | None = Field(None)


class ServiceAddTransactionRequestDTO(BaseModel):
    id: int
    count: int | None = Field(None)
    duration: int | None = Field(None)


class FineAddTransactionRequestDTO(BaseModel):
    id: int
    count: int = Field(1)


class RoomType(str, Enum):
    four_bed = 'fourBed'
    six_bed = 'sixBed'
    eight_bed = 'eightBed'


class RoomAddTransactionRequestDTO(BaseModel):
    number: str
    type: RoomType
    building: int
    count_days: int | None = Field(None, alias='countDays')


class AddTransactionRequestDTO(BaseModel):
    guest: GuestAddTransactionRequestDTO
    services: list[ServiceAddTransactionRequestDTO] | None = Field(None)
    fines: list[FineAddTransactionRequestDTO] | None = Field(None)
    room: RoomAddTransactionRequestDTO
    payment_summ: int = Field(alias='paymentSumm')
    payment_type: str = Field(alias='paymentType')

    @model_validator(mode='after')
    def check_services_or_fines(self):
        """Разрешено только одно из полей: services или fines"""
        has_services = bool(self.services)
        has_fines = bool(self.fines)
        if has_services and has_fines:
            raise ValueError("Должно быть заполнено только одно из полей: services или fines")
        return self


class AddTransactionResponseDTO(BaseModel):
    transaction_id: int
    detail: str
