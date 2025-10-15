from sqlalchemy import select, and_

from api.configs.database import async_session_maker
from modules.hotel.models.models import RoomPrice, Service, Fine
from api.configs.loggers import logger
from scripts.room_prices_data import room_prices_data


async def set_room_and_service():
    """
    Создаёт тестовые (моковые) записи комнат и услуг в базе данных.
    """

    # Моковые данные для услуг
    services_data = [
        {"name": "Лёгкая уборка комнаты", "price": 30000, "tax": 20, "is_countable": True},
        {"name": "Мойка и разморозка холодильника", "price": 25000, "tax": 20, "is_countable": True},
        {"name": "Генеральная уборка комнаты", "price": 60000, "tax": 20, "is_countable": True},
        {"name": "Стирка одного комплекта", "price": 35000, "tax": 20, "is_countable": True},
        {"name": "Замена постельного белья", "price": 25000, "tax": 20, "is_countable": True},
        {"name": "Место для легкового", "price": 5000, "tax": 20, "is_duration": True},
        {"name": "Место для Газели", "price": 10000, "tax": 20, "is_duration": True},
        {"name": "Место для микроавтобуса", "price": 15000, "tax": 20, "is_duration": True},
        {"name": "Место для автобуса", "price": 20000, "tax": 20, "is_duration": True},
    ]

    fines_data = [
        {'name': 'Подушка', 'price': 150000, 'type': 'damageToProperty'},
        {'name': 'Одеяло', 'price': 200000, 'type': 'damageToProperty'},
        {'name': 'Матрац', 'price': 700000, 'type': 'damageToProperty'},
        {'name': 'Комплект постельного белья', 'price': 200000, 'type': 'damageToProperty'},
        {'name': 'Кровать односпальная', 'price': 580000, 'type': 'damageToProperty'},
        {'name': 'Кровать двуспальная', 'price': 850000, 'type': 'damageToProperty'},
        {'name': 'Штора', 'price': 200000, 'type': 'damageToProperty'},
        {'name': 'Карниз', 'price': 150000, 'type': 'damageToProperty'},
        {'name': 'Стол', 'price': 300000, 'type': 'damageToProperty'},
        {'name': 'Стул', 'price': 200000, 'type': 'damageToProperty'},
        {'name': 'Табурет', 'price': 100000, 'type': 'damageToProperty'},
        {'name': 'Вешалка настенная', 'price': 200000, 'type': 'damageToProperty'},
        {'name': 'Шкаф-стеллаж', 'price': 400000, 'type': 'damageToProperty'},
        {'name': 'Шкаф двустворчатый', 'price': 1200000, 'type': 'damageToProperty'},
        {'name': 'Шкаф трёхстворчатый', 'price': 1800000, 'type': 'damageToProperty'},
        {'name': 'Светильник потолочный', 'price': 400000, 'type': 'damageToProperty'},
        {'name': 'Дверь металлическая входная в номер (с коробкой)', 'price': 1800000,
         'type': 'damageToProperty'},
        {'name': 'Дверь деревянная входная в номер (в сборе)', 'price': 800000,
         'type': 'damageToProperty'},
        {'name': 'Дверь деревянная входная в номер (полотно)', 'price': 500000,
         'type': 'damageToProperty'},
        {'name': 'Дверь деревянная санузловая', 'price': 350000, 'type': 'damageToProperty'},
        {'name': 'Замок двери для входной двери (в корпусе)', 'price': 300000,
         'type': 'damageToProperty'},
        {'name': 'Замок санузловой двери', 'price': 100000, 'type': 'damageToProperty'},
        {'name': 'Ручка входной двери (металл)', 'price': 300000, 'type': 'damageToProperty'},
        {'name': 'Ручка входной двери (дерево)', 'price': 150000, 'type': 'damageToProperty'},
        {'name': 'Личинка с ключами замка входной двери в номер', 'price': 100000,
         'type': 'damageToProperty'},
        {'name': 'Картина', 'price': 450000, 'type': 'damageToProperty'},
        {'name': 'Телевизор', 'price': 3500000, 'type': 'damageToProperty'},
        {'name': 'Холодильник', 'price': 3500000, 'type': 'damageToProperty'},
        {'name': 'Холодильник в комнате', 'price': 3500000, 'type': 'damageToProperty'},
        {'name': 'Варочная электрическая панель', 'price': 1800000, 'type': 'damageToProperty'},
        {'name': 'Термопот', 'price': 180000, 'type': 'damageToProperty'},
        {'name': 'Микроволновая печь', 'price': 800000, 'type': 'damageToProperty'},
        {'name': 'Унитаз', 'price': 500000, 'type': 'damageToProperty'},
        {'name': 'Сиденье для унитаза', 'price': 80000, 'type': 'damageToProperty'},
        {'name': 'Сушилка для белья', 'price': 150000, 'type': 'damageToProperty'},
        {'name': 'Стоимость дополнительной уборки помещения',
         'price': 400000, 'type': 'damageToProperty'},
        {'name': 'Штраф за несоблюдение чистоты и порядка в комнате', 'price': 200000,
         'type': 'damageToProperty'},
        {'name': 'Использование в комнате электронагревателей, электроплиток, микроволновых печей',
         'price': 200000, 'type': 'damageToProperty'},
        {'name': 'Действия, препятствующие или ограничивающие работу датчика пожарной сигнализации',
         'price': 1000000, 'type': 'damageToProperty'},
    ]

    async with async_session_maker() as session:
        # Добавляем услуги (если их нет)
        for data in services_data:
            exists = await session.scalar(select(Service).where(Service.name == data["name"]))
            if not exists:
                service = Service(**data)
                session.add(service)
                logger.info(f"Добавлена услуга: {service.name}")

        # Добавляем штрафы (если их нет)
        for data in fines_data:
            exists = await session.scalar(select(Fine).where(Fine.name == data["name"]))
            if not exists:
                fine = Fine(**data)
                session.add(fine)
                logger.info(f"Добавлен штраф: {fine.name}")

        for data in room_prices_data:
            exists = await session.scalar(
                select(RoomPrice).where(
                    and_(
                        RoomPrice.building == data["building"],
                        RoomPrice.room_type == data["room_type"],
                        RoomPrice.count_days == data["count_days"],
                    )
                )
            )
            if not exists:
                room_price = RoomPrice(**data)
                session.add(room_price)
                logger.info(f"Добавлен прайс")

        await session.commit()
