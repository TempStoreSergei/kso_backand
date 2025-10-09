from fastapi import Depends

from api.DTO.endpoints.guests.add_service_dto import AddServiceRequestDTO, AddServiceResponseDTO
from api.db.guest_repository import ServiceDatabaseRepository
from api.dependencies.get_obj_db import get_service_repo


async def add_service(
    service_data: AddServiceRequestDTO,
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
):
    service = await service_repo.create(**service_data.model_dump())
    return AddServiceResponseDTO(
        id=service.id,
        detail='Услуга добавлена успешно',
    )
