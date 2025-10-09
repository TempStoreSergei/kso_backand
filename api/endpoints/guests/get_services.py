from fastapi import Depends

from api.DTO.endpoints.guests.get_services_response_dto import GetServicesResponseDTO
from api.db.guest_repository import ServiceDatabaseRepository
from api.dependencies.get_obj_db import get_service_repo
from api.utils.notifications.send_tg_notifications import send_to_channel


async def get_services(
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
):
    await send_to_channel('Уведомление в тг!!!')
    services = await service_repo.get_all()
    services_response = []
    for service in services:
        if not service.is_deleted:
            services_response.append(service)

    return GetServicesResponseDTO(
        services=services_response
    )
