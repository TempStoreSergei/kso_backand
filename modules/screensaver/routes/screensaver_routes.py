from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.screensaver.DTO.add_file_dto import AddFileResponseDTO
from modules.screensaver.DTO.get_files_dto import GetFilesResponseDTO
from modules.screensaver.DTO.get_settings_dto import GetSettingsResponseDTO
from modules.screensaver.DTO.upadte_file_dto import UpdateFileResponseDTO
from modules.screensaver.DTO.update_settings_dto import UpdateSettingsResponseDTO
from modules.screensaver.endpoints.add_file import add_file
from modules.screensaver.endpoints.delete_file import delete_file
from modules.screensaver.endpoints.get_files import get_files
from modules.screensaver.endpoints.get_settings import get_settings
from modules.screensaver.endpoints.update_file import update_file
from modules.screensaver.endpoints.update_settings import update_settings

SCREENSAVER_ROUTES = [
    RouteDTO(
        path="/add_file",
        endpoint=add_file,
        response_model=AddFileResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_201_CREATED,
        summary="Добавление файла заставки",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/delete_file",
        endpoint=delete_file,
        response_model=None,
        methods=["DELETE"],
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Удаление файла заставки",
        description="",
        responses={
            status.HTTP_204_NO_CONTENT: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/get_files",
        endpoint=get_files,
        response_model=GetFilesResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Получение файлов заставки",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/update_file",
        endpoint=update_file,
        response_model=UpdateFileResponseDTO,
        methods=["PUT"],
        status_code=status.HTTP_200_OK,
        summary="Изменение файла заставки",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/get_settings",
        endpoint=get_settings,
        response_model=GetSettingsResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Получение настроек заставки",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/update_settings",
        endpoint=update_settings,
        response_model=UpdateSettingsResponseDTO,
        methods=["PUT"],
        status_code=status.HTTP_200_OK,
        summary="Обновление настроек заставки",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]
