from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.hotel.DTO.services.add_service_dto import AddServiceResponseDTO
from modules.hotel.DTO.services.get_services_response_dto import GetServicesResponseDTO
from modules.hotel.DTO.services.update_service_dto import UpdateServiceResponseDTO
from modules.hotel.endpoints.services.add_service import add_service
from modules.hotel.endpoints.services.delete_service import delete_service
from modules.hotel.endpoints.services.get_services import get_services
from modules.hotel.endpoints.services.update_service import update_service

SERVICES_ROUTES = [
    RouteDTO(
        path="/get_services",
        endpoint=get_services,
        response_model=GetServicesResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/add_services",
        endpoint=add_service,
        response_model=AddServiceResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_201_CREATED,
        summary="",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/delete_service",
        endpoint=delete_service,
        response_model=None,
        methods=["DELETE"],
        status_code=status.HTTP_204_NO_CONTENT,
        summary="",
        description="",
        responses={
            status.HTTP_204_NO_CONTENT: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/update_service",
        endpoint=update_service,
        response_model=UpdateServiceResponseDTO,
        methods=["PUT"],
        status_code=status.HTTP_200_OK,
        summary="",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
