from api.configs.database import async_session_maker
from modules.screensaver.models.models import ScreensaverSettings
from api.configs.loggers import logger


async def set_screensaver():
    async with async_session_maker() as session:
        exists = await session.get(ScreensaverSettings, 1)
        if exists:
            logger.info('Настройки скринсейвера уже сущестуют')
            return
        screensaver_settings = ScreensaverSettings(
            is_enable=True,
            sound_is_enable=True,
            time_show_image=200,
            idle_time=100,
            show_clock=True,
        )
        session.add(screensaver_settings)
        await session.commit()
        logger.info('Настройки скринсевера установлены')
