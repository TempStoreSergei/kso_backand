from fastapi import Depends, HTTPException, status

from modules.screensaver.DTO.update_settings_dto import UpdateSettingsResponseDTO, \
    UpdateSettingsRequestDTO
from modules.screensaver.db.screensaver_repository import ScreensaverSettingsDatabaseRepository, \
    get_screensaver_settings_repo


async def update_settings(
    update_data: UpdateSettingsRequestDTO,
    screensaver_settings_repo: ScreensaverSettingsDatabaseRepository = Depends(get_screensaver_settings_repo),
):
    settings = await screensaver_settings_repo.get(id=1)

    if not settings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Настройка заставки не заданы',
        )

    update_data_values = {}

    if update_data.is_enable is not None:
        update_data_values['is_enable'] = update_data.is_enable
    if update_data.sound_is_enable is not None:
        update_data_values['sound_is_enable'] = update_data.sound_is_enable
    if update_data.time_show_image is not None:
        update_data_values['time_show_image'] = update_data.time_show_image
    if update_data.idle_time is not None:
        update_data_values['idle_time'] = update_data.idle_time
    if update_data.show_clock is not None:
        update_data_values['show_clock'] = update_data.show_clock

    await screensaver_settings_repo.update(
        filters={'id': 1},
        values=update_data_values,
    )

    return UpdateSettingsResponseDTO(detail='Настройки заставки обновлены успешно')
