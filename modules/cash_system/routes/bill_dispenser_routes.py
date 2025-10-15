from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.cash_system.DTO.bill_acceptor.reset_bill_count_response_dto import \
    ResetBillCountResponseDTO
from modules.cash_system.DTO.bill_dispenser.add_bill_count_dto import AddBillCountResponseDTO
from modules.cash_system.DTO.bill_dispenser.bill_dispenser_status_response_dto import \
    BillDispenserStatusResponseDTO
from modules.cash_system.DTO.bill_dispenser.set_nominal_dto import SetNominalResponseDTO
from modules.cash_system.DTO.bill_dispenser.test_bill_dispense_response_DTO import \
    TestBillDispenseResponseDTO
from modules.cash_system.endpoints.bill_dispenser.reset_bill_count import reset_bill_count
from modules.cash_system.endpoints.bill_dispenser.add_bill_count import add_bill_count
from modules.cash_system.endpoints.bill_dispenser.bill_dispenser_status import bill_dispenser_status
from modules.cash_system.endpoints.bill_dispenser.set_nominal import set_nominal
from modules.cash_system.endpoints.bill_dispenser.test_bill_dispense import test_bill_dispenser

BILL_DISPENSER_ROUTES = [
    RouteDTO(
        path="/test_bill_dispenser",
        endpoint=test_bill_dispenser,
        response_model=TestBillDispenseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Тест выдачи купюр",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/add_bill_count",
        endpoint=add_bill_count,
        response_model=AddBillCountResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Добавление купюр диспенсера",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/reset_bill_count",
        endpoint=reset_bill_count,
        response_model=ResetBillCountResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Сброс количества купюр диспенсера",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/set_nominal",
        endpoint=set_nominal,
        response_model=SetNominalResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Установка номиналов купюр диспенсера",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/status",
        endpoint=bill_dispenser_status,
        response_model=BillDispenserStatusResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Установка номиналов купюр диспенсера",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
