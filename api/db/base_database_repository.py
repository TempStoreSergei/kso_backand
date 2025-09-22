from abc import ABC
from typing import Type
from uuid import UUID

from fastapi import HTTPException
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
    async def create(self, create_data: dict):
        """Базовый метод создания записи"""
        new_instance = self.model_class(**create_data)
        self.session.add(new_instance)

        await self.session.commit()
        await self.session.refresh(new_instance)
        return new_instance

    @handle_db_error
    async def read_all(self, query: select = None):
        if query is None:
            query = select(self.model_class)
        result = await self.session.execute(query)
        instances = result.scalars().all()
        return instances

    @handle_db_error
    async def read_by_id(self, instance_id: int | UUID, options: list | None = None):
        instance = await self.session.get(self.model_class, instance_id, options=options)
        if not instance:
            return None
        return instance

    @handle_db_error
    async def update(self, instance_id: int, updated_data: dict, query: select = None):
        if query is None:
            query = select(self.model_class).where(self.model_class.id == instance_id)
        result = await self.session.execute(query)
        instance = result.scalar_one_or_none()

        if not instance:
            raise HTTPException(status_code=404, detail="Объект не найден в базе данных")

        for key, value in updated_data.items():
            setattr(instance, key, value)

        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    @handle_db_error
    async def delete(self, instance_id: int):
        stmt = select(self.model_class).where(self.model_class.id == instance_id)
        result = await self.session.execute(stmt)
        instance = result.scalar_one_or_none()

        if not instance:
            raise HTTPException(status_code=404, detail="Объект не найден в базе данных")

        await self.session.delete(instance)
        await self.session.commit()
