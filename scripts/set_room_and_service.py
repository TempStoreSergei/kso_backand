from sqlalchemy import select

from api.configs.database import async_session_maker
from api.models.guests_models import Room, Service
from api.configs.loggers import logger


async def set_room_and_service():
    """
    Создаёт тестовые (моковые) записи комнат и услуг в базе данных.
    """

    # Моковые данные для услуг
    services_data = [
        {"name": "Парковка", "price": 1000, "tax": 20},
        {"name": "Завтрак", "price": 500, "tax": 10},
        {"name": "Поздний выезд", "price": 700, "tax": 15},
        {"name": "Уборка номера", "price": 300, "tax": 10},
        {"name": "Мини-бар", "price": 1500, "tax": 20},
        {"name": "Спа", "price": 2500, "tax": 20},
        {"name": "Трансфер", "price": 1200, "tax": 20},
        {"name": "Аренда конференц-зала", "price": 5000, "tax": 20},
        {"name": "Прачечная", "price": 800, "tax": 15},
        {"name": "Wi-Fi Premium", "price": 300, "tax": 10},
    ]

    # Моковые данные для комнат
    rooms_data = [
        {"name": f"{i + 1}"}
        for i in range(30)
    ]

    async with async_session_maker() as session:
        # Добавляем услуги (если их нет)
        for data in services_data:
            exists = await session.scalar(select(Service).where(Service.name == data["name"]))
            if not exists:
                service = Service(**data)
                session.add(service)
                logger.info(f"Добавлена услуга: {service.name}")

        # Добавляем комнаты (если их нет)
        for data in rooms_data:
            exists = await session.scalar(select(Room).where(Room.name == data["name"]))
            if not exists:
                room = Room(**data)
                session.add(room)
                logger.info(f"Добавлена комната: {room.name}")

        await session.commit()
