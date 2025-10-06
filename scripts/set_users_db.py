from sqlalchemy import select

from api.configs.database import async_session_maker
from api.models.auth_models import User
from api.configs.loggers import logger
from api.utils.auth.devpass import hash_password


async def set_users_db():
    """Функция заполняет таблицу пользователей в базе данных."""

    users = [
        {
            'username': 'admin1',
            'password': 'admin1',
            'role': 'admin',
        },
        {
            'username': 'operator',
            'password': 'operator',
            'role': 'operator',
        },
    ]

    async with async_session_maker() as session:
        for user in users:
            # проверяем, есть ли пользователь
            db_user = await session.scalar(
                select(User).where(User.username == user["username"])
            )
            if db_user:
                continue
            hashed = hash_password(user["password"])
            user_data = User(username=user["username"], password=hashed, role=user["role"])
            session.add(user_data)
            logger.info(f'Добавлен пользователь {user_data.username}')
        await session.commit()
