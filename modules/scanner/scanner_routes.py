from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.scanner.send_scanned_code_dto import SendScannedCodeResponseDTO
from modules.scanner.send_scanner_code_endpoint import send_scanned_code


SCANNER = [
    RouteDTO(
        path="/send_scanned_code",
        endpoint=send_scanned_code,
        response_model=SendScannedCodeResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Получение кода со сканера",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
