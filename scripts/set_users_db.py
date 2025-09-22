from sqlalchemy import select

from api.configs.database import async_session_maker
from api.models.auth_models import User
from api.configs.loggers import logger


async def set_users_db():
    """Функция заполняет таблицу пользователей в базе данных."""

    users = [
        {
            'user_name': 'admin',
            'user_password': 'admin',
        },
        {
            'user_name': 'operator',
            'user_password': 'operator',
        },
    ]

    async with async_session_maker() as session:
        for user in users:
            # проверяем, есть ли пользователь
            db_user = await session.scalar(
                select(User).where(User.user_name == user["user_name"])
            )
            if db_user:
                continue
            user_data = User(**user)
            session.add(user_data)
            logger.info(f'Добавлен пользователь {user_data.user_name}')
        await session.commit()
