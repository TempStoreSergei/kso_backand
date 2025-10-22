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
        {"name": "Простая уборка комнаты", "price": 30000, "tax": 20, "is_countable": True,
         "code": '901'},
        {"name": "Услуга по мойке и разморозке холодильника", "price": 25000, "tax": 20,
         "is_countable": True, "code": '902'},
        {"name": "Генеральная уборка комнаты", "price": 60000, "tax": 20, "is_countable": True,
         "code": '903'},
        {"name": "Жетон для стиральной машины", "price": 35000, "tax": 20, "is_countable": True,
         "code": '904'},
        {"name": "Замена постельного белья", "price": 25000, "tax": 20, "is_countable": True,
         "code": '905'},

        {"name": "Размещение легкового автомобиля", "price": 5000, "tax": 20, "is_duration": True,
         "code": '700'},
        {"name": "Размещение грузового транспорта (автомобили типа 'Газель')", "price": 10000,
         "tax": 20, "is_duration": True, "code": '701'},
        {"name": "Размещение микроавтобусов (Форд, Ситроен и аналогичные)", "price": 15000,
         "tax": 20, "is_duration": True, "code": '702'},
        {"name": "Размещение пассажирского автотранспорта (ПАЗ и аналогичные)", "price": 20000,
         "tax": 20, "is_duration": True, "code": '703'},
    ]

    code_violation = 100
    fines_data = [
        {'name': 'Штраф за несоблюдение чистоты и порядка в комнате', 'price': 200000,
         'type': 'violationRules', 'code': 'нп1'},
        {'name': 'Использование в комнате электрочайников, электроплиток, микроволновых печей',
         'price': 200000, 'type': 'violationRules', 'code': 'нп2'},
        {
            'name': 'Нарушение тишины, покоя, общественного порядка в будние дни с 21-00 до 08-00, выходные и праздничные дни с 22-00 до 10-00',
            'price': 100000, 'type': 'violationRules', 'code': 'нп3'},
        {'name': 'Пронос алкогольных напитков (в т.ч. пиво, коктейли)', 'price': 100000,
         'type': 'violationRules', 'code': 'нп4'},
        {'name': 'Распитие алкогольных напитков (в т.ч. пиво, коктейли)', 'price': 100000,
         'type': 'violationRules', 'code': 'нп5'},
        {'name': 'Нахождение в состоянии алкогольного или наркотического опьянения',
         'price': 100000, 'type': 'violationRules', 'code': 'нп6'},
        {
            'name': 'Курение (в т.ч. электронных сигарет в помещениях хостела, а не в отведенных для этого местах)',
            'price': 100000, 'type': 'violationRules', 'code': 'нп7'},
        {'name': 'В случае срабатывания пожарной сигнализации (курение, парение)', 'price': 200000,
         'type': 'violationRules', 'code': 'нп8'},
        {
            'name': 'Вмешательство в работу пожарной сигнализации путем демонтажа или закрытия датчика пожарной сигнализации',
            'price': 500000, 'type': 'violationRules', 'code': 'нп9'},
        {'name': 'Использование мощных электронагревательных приборов без согласования',
         'price': 100000, 'type': 'violationRules', 'code': 'нп10'},
        {'name': 'Вынос ключа от комнаты за территорию Хостела', 'price': 50000,
         'type': 'violationRules', 'code': 'нп11'},
    ]

    fines_data += [
        {'name': 'Варочная Электрическая панель', 'price': 1800000, 'type': 'damageToProperty',
         'code': '629'},
        {'name': 'Вешалка настенная', 'price': 140000, 'type': 'damageToProperty', 'code': '611'},
        {'name': 'Дверь деревянная входная в номер (в сборе)', 'price': 800000,
         'type': 'damageToProperty', 'code': '617'},
        {'name': 'Дверь деревянная входная в номер (полотно)', 'price': 500000,
         'type': 'damageToProperty', 'code': '618'},
        {'name': 'Дверь деревянная санузловая', 'price': 500000, 'type': 'damageToProperty',
         'code': '619'},
        {'name': 'Дверь металлическая входная в номер (с коробкой)', 'price': 3600000,
         'type': 'damageToProperty', 'code': '616'},
        {
            'name': 'Действия, препятствующие или ограничивающие работу датчика пожарной сигнализации, а также его демонтаж (на всю комнату)',
            'price': 1000000, 'type': 'damageToProperty', 'code': '639'},
        {'name': 'Замок двери для входной двери (в корпус)', 'price': 300000,
         'type': 'damageToProperty', 'code': '620'},
        {'name': 'Замок санузловой двери', 'price': 300000, 'type': 'damageToProperty',
         'code': '621'},
        {'name': 'Карниз', 'price': 200000, 'type': 'damageToProperty', 'code': '607'},
        {'name': 'Картина', 'price': 450000, 'type': 'damageToProperty', 'code': '625'},
        {'name': 'Комплект постельного белья', 'price': 200000, 'type': 'damageToProperty',
         'code': '603'},
        {'name': 'Кровать двухярусная', 'price': 850000, 'type': 'damageToProperty', 'code': '605'},
        {'name': 'Кровать одноярусная', 'price': 580000, 'type': 'damageToProperty', 'code': '604'},
        {'name': 'Личинка с ключами замка входной двери в номер', 'price': 200000,
         'type': 'damageToProperty', 'code': '624'},
        {'name': 'Матрац', 'price': 700000, 'type': 'damageToProperty', 'code': '602'},
        {'name': 'Микроволновая печь', 'price': 1600000, 'type': 'damageToProperty', 'code': '631'},
        {'name': 'Одеяло', 'price': 200000, 'type': 'damageToProperty', 'code': '601'},
        {'name': 'Подушка', 'price': 150000, 'type': 'damageToProperty', 'code': '600'},
        {'name': 'Ручка входной двери деревянная', 'price': 150000, 'type': 'damageToProperty',
         'code': '623'},
        {'name': 'Ручка входной двери металл', 'price': 300000, 'type': 'damageToProperty',
         'code': '622'},
        {'name': 'Светильник потолочный', 'price': 400000, 'type': 'damageToProperty', 'code': '615'},
        {'name': 'Сиденье для унитаза', 'price': 200000, 'type': 'damageToProperty', 'code': '633'},
        {'name': 'Стоимость дополнительной уборки помещения', 'price': 400000,
         'type': 'damageToProperty', 'code': '637'},
        {'name': 'Стол', 'price': 500000, 'type': 'damageToProperty', 'code': '608'},
        {'name': 'Стул', 'price': 300000, 'type': 'damageToProperty', 'code': '609'},
        {'name': 'Сушилка для белья', 'price': 500000, 'type': 'damageToProperty', 'code': '634'},
        {'name': 'Табурет', 'price': 100000, 'type': 'damageToProperty', 'code': '610'},
        {'name': 'Телевизор', 'price': 4000000, 'type': 'damageToProperty', 'code': '626'},
        {'name': 'Термопот', 'price': 4000000, 'type': 'damageToProperty', 'code': '630'},
        {'name': 'Унитаз', 'price': 800000, 'type': 'damageToProperty', 'code': '632'},
        {'name': 'Утюг', 'price': 800000, 'type': 'damageToProperty', 'code': '635'},
        {'name': 'Холодильник в комнате', 'price': 3500000, 'type': 'damageToProperty',
         'code': '628'},
        {'name': 'Холодильный шкаф', 'price': 8500000, 'type': 'damageToProperty', 'code': '627'},
        {'name': 'Шкаф двустворчатый', 'price': 1200000, 'type': 'damageToProperty', 'code': '613'},
        {'name': 'Шкаф трёхстворчатый', 'price': 1800000, 'type': 'damageToProperty', 'code': '614'},
        {'name': 'Шкаф-стеллаж', 'price': 400000, 'type': 'damageToProperty', 'code': '612'},
        {'name': 'Штора', 'price': 150000, 'type': 'damageToProperty', 'code': '606'},
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
