from fastapi import Depends, HTTPException, status

from modules.hotel.db.services_repository import ServiceDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_service_repo


async def delete_service(
    service_id: int,
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
):
    deleted_service = await service_repo.soft_delete(id=service_id)
    if not deleted_service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Услуга не найдена'
        )
    return
