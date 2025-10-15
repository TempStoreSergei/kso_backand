from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from api.DTO.system.check_system_dto import CheckSystemResponseDTO
from api.DTO.system.set_used_hadrware_dto import SetUsedHardwareResponseDTO
from api.endpoints.system.check_system import check_system
from api.endpoints.system.set_used_hardware import set_used_hardware

SYSTEM_ROUTES = [
    RouteDTO(
        path="/check_system",
        endpoint=check_system,
        response_model=CheckSystemResponseDTO,
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
        path="/set_used_hardware",
        endpoint=set_used_hardware,
        response_model=SetUsedHardwareResponseDTO,
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
    # RouteDTO(
    #     path="/shutdown",
    #     endpoint=login,
    #     response_model=LoginResponseDTO,
    #     methods=["POST"],
    #     status_code=status.HTTP_200_OK,
    #     summary="",
    #     description="",
    #     responses={
    #         status.HTTP_200_OK: {
    #             "description": "",
    #         },
    #     },
    # ),
    # RouteDTO(
    #     path="/reboot",
    #     endpoint=login,
    #     response_model=LoginResponseDTO,
    #     methods=["POST"],
    #     status_code=status.HTTP_200_OK,
    #     summary="",
    #     description="",
    #     responses={
    #         status.HTTP_200_OK: {
    #             "description": "",
    #         },
    #     },
    # ),
]
