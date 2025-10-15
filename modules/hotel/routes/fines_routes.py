from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.hotel.DTO.fines.add_fine_dto import AddFineResponseDTO
from modules.hotel.DTO.fines.get_fines_dto import GetFinesResponseDTO
from modules.hotel.DTO.fines.update_fine_dto import UpdateFineResponseDTO
from modules.hotel.endpoints.fines.add_fine import add_fine
from modules.hotel.endpoints.fines.delete_fine import delete_fine
from modules.hotel.endpoints.fines.get_fines import get_fines
from modules.hotel.endpoints.fines.update_fine import update_fine

FINES_ROUTES = [
    RouteDTO(
        path="/add_fine",
        endpoint=add_fine,
        response_model=AddFineResponseDTO,
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
        path="/get_fines",
        endpoint=get_fines,
        response_model=GetFinesResponseDTO,
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
        path="/delete_fine",
        endpoint=delete_fine,
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
        path="/update_fine",
        endpoint=update_fine,
        response_model=UpdateFineResponseDTO,
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
