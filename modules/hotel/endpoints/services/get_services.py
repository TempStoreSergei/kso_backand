from fastapi import Depends

from modules.hotel.DTO.services.get_services_response_dto import GetServicesResponseDTO
from modules.hotel.db.services_repository import ServiceDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_service_repo


async def get_services(
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
):
    services = await service_repo.get_all()
    services_response = []
    for service in services:
        if not service.is_deleted:
            services_response.append(service)

    return GetServicesResponseDTO(
        services=services_response
    )
