from fastapi import Depends, HTTPException, status

from modules.hotel.DTO.transactions.calculate_room_price_dto import CalculateRoomPriceRequestDTO, \
    CalculateRoomPriceResponseDTO
from modules.hotel.db.fines_repository import FineDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_room_price_repo


async def calculate_room_price(
    calculated_data: CalculateRoomPriceRequestDTO,
    room_price_repo: FineDatabaseRepository = Depends(get_room_price_repo),
):
    if calculated_data.count_days > 60:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Оплатить можно не более 60 дней'
        )
    room_price_obj = await room_price_repo.get(
        building=calculated_data.room_building,
        room_type=calculated_data.room_type,
        count_days=calculated_data.count_days
    )

    if not room_price_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не найдено корректное значение стоимости номера'
        )

    summ_room_price = room_price_obj.price * room_price_obj.count_days

    return CalculateRoomPriceResponseDTO(summ_room_price=summ_room_price)
