from fastapi import Depends, HTTPException, status

from api.db.guest_repository import RoomDatabaseRepository
from api.dependencies.get_obj_db import get_room_repo


async def delete_room(
    room_id: int,
    room_repo: RoomDatabaseRepository = Depends(get_room_repo),
):
    deleted_room = await room_repo.soft_delete(id=room_id)
    if not deleted_room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Комната не найдена'
        )
    return
