from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.cash_system.DTO.coin_system.add_coin_count_dto import AddCoinCountResponseDTO
from modules.cash_system.DTO.coin_system.cash_collection_response_dto import \
    CashCollectionResponseDTO
from modules.cash_system.DTO.coin_system.test_coin_accept_response_dto import \
    TestCoinAcceptResponseDTO
from modules.cash_system.DTO.coin_system.test_coin_dispense_response_dto import \
    TestCoinDispenseResponseDTO
from modules.cash_system.endpoints.coin_system.add_coin_count import add_coin_count
from modules.cash_system.endpoints.coin_system.cash_collection import cash_collection
from modules.cash_system.endpoints.coin_system.test_coin_accept import test_coin_accept
from modules.cash_system.endpoints.coin_system.test_coin_dispense import test_coin_dispense

COIN_SYSTEM_ROUTES = [
    RouteDTO(
        path="/test_coin_accept",
        endpoint=test_coin_accept,
        response_model=TestCoinAcceptResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Тест приема монет",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/test_coin_dispense",
        endpoint=test_coin_dispense,
        response_model=TestCoinDispenseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Тест выдачи монет",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/add_coin_count",
        endpoint=add_coin_count,
        response_model=AddCoinCountResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Добавление монет",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/cash_collection",
        endpoint=cash_collection,
        response_model=CashCollectionResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Инкассация монет",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
