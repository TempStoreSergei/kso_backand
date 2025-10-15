from fastapi import Depends, HTTPException, status

from modules.hotel.db.fines_repository import FineDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_fine_repo


async def delete_fine(
    fine_id: int,
    fine_repo: FineDatabaseRepository = Depends(get_fine_repo),
):
    deleted_fine = await fine_repo.soft_delete(id=fine_id)
    if not deleted_fine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Штраф не найден'
        )
    return