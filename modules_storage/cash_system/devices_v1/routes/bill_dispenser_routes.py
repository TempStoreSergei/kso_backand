from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.cash_system.DTO.bill_dispenser.test_bill_dispense_response_DTO import \
    TestBillDispenseResponseDTO
from modules.cash_system.endpoints.bill_dispenser.test_bill_dispense import test_bill_dispenser

BILL_DISPENSER_ROUTES = [
    RouteDTO(
        path="/test",
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
]
