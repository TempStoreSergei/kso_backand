from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.cash_system.DTO.bill_acceptor.bill_acceprot_status_response_dto import \
    BillAcceptorStatusResponseDTO
from modules.cash_system.DTO.bill_acceptor.reset_bill_count_response_dto import \
    ResetBillCountResponseDTO
from modules.cash_system.DTO.bill_acceptor.set_max_bill_count_response_dto import \
    SetMaxBillCountResponseDTO
from modules.cash_system.DTO.bill_acceptor.test_bill_accept_dto import \
    TestBillAcceptResponseDTO
from modules.cash_system.endpoints.bill_acceptor.bill_acceprot_status import bill_acceptor_status
from modules.cash_system.endpoints.bill_acceptor.reset_bill_count import reset_bill_count
from modules.cash_system.endpoints.bill_acceptor.set_max_bill_count import set_max_bill_count
from modules.cash_system.endpoints.bill_acceptor.test_bill_accept import test_bill_accept

BILL_ACCEPTOR_ROUTES = [
    RouteDTO(
        path="/test_bill_accept",
        endpoint=test_bill_accept,
        response_model=TestBillAcceptResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Тест приема купюр",
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
        summary="Сброс количества купюр в купюроприемнике (инкасация)",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/set_max_bill_count",
        endpoint=set_max_bill_count,
        response_model=SetMaxBillCountResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Установка максимального количества купюр в купюроприемнике",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/status",
        endpoint=bill_acceptor_status,
        response_model=BillAcceptorStatusResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Статус купюроприемника",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
