from fastapi import Depends, HTTPException, status

from modules.screensaver.DTO.get_settings_dto import GetSettingsResponseDTO
from modules.screensaver.db.screensaver_repository import ScreensaverSettingsDatabaseRepository, \
    get_screensaver_settings_repo


async def get_settings(
    screensaver_settings_repo: ScreensaverSettingsDatabaseRepository = Depends(get_screensaver_settings_repo),
):
    settings = await screensaver_settings_repo.get(id=1)
    if not settings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Настройка заставки не заданы',
        )
    return GetSettingsResponseDTO.model_validate(settings)
