from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.cash_system.DTO.set_available_devices_dto import SetAvailableDevicesResponseDTO
from modules.cash_system.DTO.start_accepting_payment_response_dto import \
    StartAcceptingPaymentResponseDTO
from modules.cash_system.DTO.stop_accepting_payment_response_dto import \
    StopAcceptingPaymentResponseDTO
from modules.cash_system.endpoints.init_system import init_system
from modules.cash_system.DTO.init_system_response_dto import InitSystemResponseDTO
from modules.cash_system.endpoints.set_available_devices import set_available_devices
from modules.cash_system.endpoints.start_accepting_payment import start_accepting_payment
from modules.cash_system.endpoints.stop_accepting_payment import stop_accepting_payment

CASH_SYSTEM_ROUTES = [
    RouteDTO(
        path="/init_system",
        endpoint=init_system,
        response_model=InitSystemResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Инициализация наличной системы оплаты",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/set_available_devices",
        endpoint=set_available_devices,
        response_model=SetAvailableDevicesResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Выбор устройств наличной системы оплаты",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/start_accepting_payment",
        endpoint=start_accepting_payment,
        response_model=StartAcceptingPaymentResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Запустить процесс оплаты наличными",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/stop_accepting_payment",
        endpoint=stop_accepting_payment,
        response_model=StopAcceptingPaymentResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Остановить/прервать процесс оплаты наличными",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
