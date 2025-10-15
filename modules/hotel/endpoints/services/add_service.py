from fastapi import Depends

from modules.hotel.DTO.services.add_service_dto import AddServiceRequestDTO, AddServiceResponseDTO
from modules.hotel.db.services_repository import ServiceDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_service_repo


async def add_service(
    service_data: AddServiceRequestDTO,
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
):
    service = await service_repo.create(**service_data.model_dump())
    return AddServiceResponseDTO(
        id=service.id,
        detail='Услуга добавлена успешно',
    )
