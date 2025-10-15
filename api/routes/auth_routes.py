from fastapi import status

from api.DTO.auth.login_dto import LoginResponseDTO
from api.DTO.auth.refresh_dto import RefreshResponseDTO
from api.DTO.auth.register_dto import RegisterResponseDTO
from api.DTO.auth.update_user_role_dto import UpdateUserRoleResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.auth.delete_user import delete_user
from api.endpoints.auth.login import login
from api.endpoints.auth.logout import logout
from api.endpoints.auth.refresh import refresh
from api.endpoints.auth.register import register
from api.endpoints.auth.update_user_role import update_user_role

AUTH_ROUTES = [
    RouteDTO(
        path="/login",
        endpoint=login,
        response_model=LoginResponseDTO,
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
        path="/logout",
        endpoint=logout,
        response_model=LoginResponseDTO,
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
        path="/refresh",
        endpoint=refresh,
        response_model=RefreshResponseDTO,
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
        path="/register",
        endpoint=register,
        response_model=RegisterResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_201_CREATED,
        summary="",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/{username}",
        endpoint=delete_user,
        response_model=None,
        methods=["DELETE"],
        status_code=status.HTTP_204_NO_CONTENT,
        summary="",
        description="",
        responses={
            status.HTTP_204_NO_CONTENT: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/{username}/role",
        endpoint=update_user_role,
        response_model=UpdateUserRoleResponseDTO,
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
]
