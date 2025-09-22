from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.cash_system.DTO.bill_acceptor.test_bill_accept_response_DTO import \
    TestBillAcceptResponseDTO
from modules.cash_system.endpoints.bill_acceptor.test_bill_accept import test_bill_accept

BILL_ACCEPTOR_ROUTES = [
    RouteDTO(
        path="/test",
        endpoint=test_bill_accept,
        response_model=TestBillAcceptResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Тест приема купюр",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
