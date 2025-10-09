from fastapi import Depends

from api.DTO.endpoints.guests.add_room_dto import AddRoomRequestDTO, AddRoomResponseDTO
from api.db.guest_repository import RoomDatabaseRepository
from api.dependencies.get_obj_db import get_room_repo


async def add_room(
    room_data: AddRoomRequestDTO,
    room_repo: RoomDatabaseRepository = Depends(get_room_repo),
):
    room = await room_repo.create(name=room_data.name)
    return AddRoomResponseDTO(id=room.id, detail='Комната добавлена успешно')
