from fastapi import Depends

from modules.hotel.DTO.services.update_service_dto import UpdateServiceRequestDTO, UpdateServiceResponseDTO
from modules.hotel.db.services_repository import ServiceDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_service_repo


async def update_service(
    updated_data: UpdateServiceRequestDTO,
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
):
    update_fields = {k: v for k, v in updated_data.dict(exclude_unset=True).items() if k != "id"}

    service = await service_repo.update(
        filters={'id': updated_data.id},
        values=update_fields
    )
    return UpdateServiceResponseDTO(
        id=service.id,
        detail='Услуга изменена успешно',
    )
