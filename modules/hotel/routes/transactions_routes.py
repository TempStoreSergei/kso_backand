from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.hotel.DTO.transactions.calculate_room_price_dto import CalculateRoomPriceResponseDTO
from modules.hotel.DTO.transactions.get_rooms_dto import GetRoomsResponseDTO
from modules.hotel.DTO.transactions.get_transactions_response_dto import GetTransactionsResponseDTO
from modules.hotel.DTO.transactions.save_transaction_dto import AddTransactionResponseDTO
from modules.hotel.DTO.transactions.update_transaction_dto import UpdateTransactionResponseDTO
from modules.hotel.endpoints.transactions.calculate_room_price import calculate_room_price
from modules.hotel.endpoints.transactions.get_rooms import get_rooms
from modules.hotel.endpoints.transactions.get_transactions import get_transactions
from modules.hotel.endpoints.transactions.save_transaction import save_transaction
from modules.hotel.endpoints.transactions.update_transaction import update_transaction

TRANSACTIONS_ROUTES = [
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
        path="/calculate_room_price",
        endpoint=calculate_room_price,
        response_model=CalculateRoomPriceResponseDTO,
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
        path="/update_transaction",
        endpoint=update_transaction,
        response_model=UpdateTransactionResponseDTO,
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
]
