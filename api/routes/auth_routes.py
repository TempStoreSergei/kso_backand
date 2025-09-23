from fastapi import status

from api.DTO.endpoints.auth.change_password_dto import ChangePasswordResponseDTO
from api.DTO.endpoints.auth.get_user_functioins_dto import GetUserFunctionsResponseDTO
from api.DTO.endpoints.auth.login_dto import LoginResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.auth.change_user_password import change_password
from api.endpoints.auth.get_user_functions import get_user_functions
from api.endpoints.auth.login import login
from api.endpoints.auth.logout import logout

AUTH_ROUTES = [
    RouteDTO(
        path="/login",
        endpoint=login,
        response_model=LoginResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_201_CREATED,
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
        response_model=None,
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
        path="/change_password",
        endpoint=change_password,
        response_model=ChangePasswordResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Изменить свой пароль ",
        description="Изменение своего пароля.",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/get_user_functions",
        endpoint=get_user_functions,
        response_model=GetUserFunctionsResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Получить функции пользователя",
        description="Получение функций пользователя.",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
