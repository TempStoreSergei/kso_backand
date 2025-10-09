from sqlalchemy import text

from api.configs.database import async_session_maker
from api.configs.loggers import logger


async def drop_tables_db():
    """Тестовая функция для очистки таблиц."""
    async with async_session_maker() as session:
        await session.execute(text(
            "TRUNCATE TABLE guests, transaction_services, services, rooms, transactions RESTART IDENTITY CASCADE"))
        await session.commit()
        logger.info('Все таблицы БД очищены')
