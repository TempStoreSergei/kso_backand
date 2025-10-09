from fastapi import Depends

from api.DTO.endpoints.guests.get_rooms_response_dto import GetRoomsResponseDTO
from api.db.guest_repository import RoomDatabaseRepository
from api.dependencies.get_obj_db import get_room_repo


async def get_rooms(
    room_repo: RoomDatabaseRepository = Depends(get_room_repo),
):
    rooms = await room_repo.get_all()
    rooms_response = []
    for room in rooms:
        if not room.is_deleted:
            rooms_response.append(room)
    return GetRoomsResponseDTO(rooms=rooms_response)
