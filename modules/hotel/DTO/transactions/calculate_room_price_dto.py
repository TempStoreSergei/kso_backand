from pydantic import BaseModel, Field

from modules.hotel.DTO.enums import RoomType


class CalculateRoomPriceRequestDTO(BaseModel):
    """DTO для расчета стоимости номера."""
    room_type: RoomType = Field(alias='roomType', description="Тип номера", examples=['fourBed'])
    room_building: int = Field(alias='roomBuilding', description="Корпус номера", examples=[1])
    count_days: int = Field(alias='countDays', description="Количество дней", examples=[5])


class CalculateRoomPriceResponseDTO(BaseModel):
    """DTO для ответа на расчет стоимости номера."""
    summ_room_price: int = Field(
        serialization_alias='summRoomPrice', description="Сумма за проживание", examples=[5000]
    )
