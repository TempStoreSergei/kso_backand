from pydantic import BaseModel, Field

from modules.hotel.DTO.transactions.save_transaction_dto import RoomType


class CalculateRoomPriceRequestDTO(BaseModel):
    room_type: RoomType = Field(alias='roomType')
    room_building: int = Field(alias='roomBuilding')
    count_days: int = Field(alias='countDays')


class CalculateRoomPriceResponseDTO(BaseModel):
    summ_room_price: int = Field(serialization_alias='summRoomRrice')
