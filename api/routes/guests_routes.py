from fastapi import status

from api.DTO.endpoints.guests.get_services_response_dto import GetServicesResponseDTO
from api.DTO.endpoints.guests.get_transactions_response_dto import GetTransactionsResponseDTO
from api.DTO.endpoints.guests.save_transaction_dto import AddTransactionResponseDTO
from api.DTO.factories.router_factory import RouteDTO
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
        path="/add_rooms",
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
        path="/get_rooms",
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
        path="/delete_rooms",
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
        path="/get_services",
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
        path="/add_services",
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
        path="/delete_services",
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
]
