from fastapi import status

from api.DTO.endpoints.guests.add_room_dto import AddRoomResponseDTO
from api.DTO.endpoints.guests.add_service_dto import AddServiceResponseDTO
from api.DTO.endpoints.guests.get_rooms_response_dto import GetRoomsResponseDTO
from api.DTO.endpoints.guests.get_services_response_dto import GetServicesResponseDTO
from api.DTO.endpoints.guests.get_transactions_response_dto import GetTransactionsResponseDTO
from api.DTO.endpoints.guests.save_transaction_dto import AddTransactionResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.guests.delete_service import delete_service
from api.endpoints.guests.add_room import add_room
from api.endpoints.guests.add_service import add_service
from api.endpoints.guests.delete_room import delete_room
from api.endpoints.guests.get_rooms import get_rooms
from api.endpoints.guests.get_services import get_services
from api.endpoints.guests.get_transactions import get_transactions
from api.endpoints.guests.save_transaction import save_transaction


GUESTS_ROUTES = [
    RouteDTO(
        path="/save_transaction",
        endpoint=save_transaction,
        response_model=AddTransactionResponseDTO,
        methods=["POST"],
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
        path="/get_transactions",
        endpoint=get_transactions,
        response_model=GetTransactionsResponseDTO,
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
        path="/add_room",
        endpoint=add_room,
        response_model=AddRoomResponseDTO,
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
        path="/get_rooms",
        endpoint=get_rooms,
        response_model=GetRoomsResponseDTO,
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
        path="/delete_room",
        endpoint=delete_room,
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
    # RouteDTO(
    #     path="/update_transaction/{transaction_id}",
    #     endpoint=get_transactions,
    #     response_model=GetTransactionsResponseDTO,
    #     methods=["GET"],
    #     status_code=status.HTTP_200_OK,
    #     summary="",
    #     description="",
    #     responses={
    #         status.HTTP_200_OK: {
    #             "description": "",
    #         },
    #     },
    # ),
]
