from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.acquiring.DTO.cancel_pay_response_dto import CancelPaymentResponseDTO
from modules.acquiring.DTO.check_connect_response_dto import CheckConnectResponseDTO
from modules.acquiring.DTO.open_menu_response_dto import OpenMenuResponseDTO
from modules.acquiring.DTO.receipt_report_response_dto import ReceiptReportResponseDTO
from modules.acquiring.DTO.refund_payment_response_dto import RefundPaymentResponseDTO
from modules.acquiring.DTO.start_payment_response_dto import StartPaymentResponseDTO
from modules.acquiring.endpoints.cancel_payment import cancel_payment
from modules.acquiring.endpoints.check_connect import check_connect
from modules.acquiring.endpoints.check_connect_old import check_connect_old
from modules.acquiring.endpoints.open_menu import open_menu
from modules.acquiring.endpoints.receipt_report import receipt_report
from modules.acquiring.endpoints.refund_payment import refund_payment
from modules.acquiring.endpoints.start_payment import start_payment


ACQUIRING = [
    RouteDTO(
        path="/start_payment",
        endpoint=start_payment,
        response_model=StartPaymentResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Начало оплаты по карте",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/refund_payment",
        endpoint=refund_payment,
        response_model=RefundPaymentResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Возврат оплаты",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/receipt_report",
        endpoint=receipt_report,
        response_model=ReceiptReportResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Сверка итогов",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/cancel_payment",
        endpoint=cancel_payment,
        response_model=CancelPaymentResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Отмена платежа",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/open_menu",
        endpoint=open_menu,
        response_model=OpenMenuResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Открыть технологическое меню",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/check_connect",
        endpoint=check_connect,
        response_model=CheckConnectResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Проверка соединения",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/check_connect_old",
        endpoint=check_connect_old,
        response_model=CheckConnectResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Проверка соединения (старая прошивка)",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
