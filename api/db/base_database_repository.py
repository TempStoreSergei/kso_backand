from abc import ABC
from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import Base
from api.db.error_handlers import handle_db_error


class BaseDatabaseRepository(ABC):
    """Базовый класс для работы с базой данных"""
    model_class: Type[Base] | None = None

    def __init__(self, session: AsyncSession):
        self.session = session

    @handle_db_error
    async def create(self, **kwargs):
        """Базовый метод создания записи"""
        new_instance = self.model_class(**kwargs)
        self.session.add(new_instance)
        await self.session.flush()
        return new_instance

    @handle_db_error
    async def get(self, **filters):
        result = await self.session.execute(select(self.model_class).filter_by(**filters))
        return result.scalars().first()

    @handle_db_error
    async def get_all(self, **filters):
        result = await self.session.execute(select(self.model_class).filter_by(**filters))
        return result.scalars().all()

    @handle_db_error
    async def update(self, filters: dict, values: dict):
        query = select(self.model_class).filter_by(**filters)
        result = await self.session.execute(query)
        obj = result.scalar_one_or_none()
        if obj:
            for k, v in values.items():
                setattr(obj, k, v)
        return obj

    @handle_db_error
    async def delete(self, **filters):
        query = select(self.model_class).filter_by(**filters)
        result = await self.session.execute(query)
        obj = result.scalar_one_or_none()
        if obj:
            await self.session.delete(obj)
        return obj

    @handle_db_error
    async def soft_delete(self, **filters):
        query = select(self.model_class).filter_by(**filters)
        result = await self.session.execute(query)
        obj = result.scalar_one_or_none()
        if obj:
            obj.is_deleted = True
        return obj
