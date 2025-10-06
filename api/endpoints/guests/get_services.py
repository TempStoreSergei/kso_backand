from fastapi import Depends

from api.DTO.endpoints.guests.get_services_response_dto import GetServicesResponseDTO
from api.db.guest_repository import ServiceDatabaseRepository
from api.dependencies.get_obj_db import get_service_repo


async def get_services(
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
):
    services = await service_repo.get_all()

    return GetServicesResponseDTO(
        services=services
    )
