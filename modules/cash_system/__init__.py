import asyncio

from api.utils.notifications.send_tg_notifications import send_to_channel
from api.dependencies.redis_connection import get_redis
from modules.cash_system.configs.settings import cash_system_settings


async def check_bill_acceptor():
    PERCENT_NOTIFICATION = 70
    async for redis in get_redis():
        max_bill_count = await redis.get('max_bill_count')
        bill_count = await redis.get('bill_count')

        if max_bill_count is None or bill_count is None:
            max_bill_count = 1450
            await redis.set('max_bill_count', max_bill_count)
            bill_count = 0
            await redis.set('bill_count', bill_count)

        # вычисляем процент заполнения
        fill_percent = int(bill_count) / int(max_bill_count) * 100

        if fill_percent >= PERCENT_NOTIFICATION:
            text = (
                "<b>⚠️ Купюроприёмник почти заполнен!</b>\n\n"
                f"<b>Текущий уровень:</b> {bill_count}\n"
                f"<b>Максимальный уровень:</b> {max_bill_count}\n"
                f"<b>Заполненность:</b> {fill_percent:.1f}%"
            )
            await send_to_channel(text)


async def check_bill_dispenser():
    PERCENT_NOTIFICATION = 20
    async for redis in get_redis():
        upper_box_count = await redis.get('bill_dispenser:upper_count')
        lower_box_count = await redis.get('bill_dispenser:lower_count')

        if upper_box_count is None or lower_box_count is None:
            upper_box_count = lower_box_count = 0
            await redis.set('bill_dispenser:upper_count', upper_box_count)
            await redis.set('bill_dispenser:lower_count', lower_box_count)

        # проверка наличия значений в redis
        upper_lvl = await redis.get('bill_dispenser:upper_lvl')
        lower_lvl = await redis.get('bill_dispenser:lower_lvl')
        if upper_lvl is None or lower_lvl is None:
            await redis.set('bill_dispenser:upper_lvl', 10000)
            await redis.set('bill_dispenser:lower_lvl', 5000)

        # вычисляем процент заполнения
        percent_upper = int(upper_box_count) / cash_system_settings.UPPER_CASSETTE_SIZE * 100
        percent_lower = int(lower_box_count) / cash_system_settings.LOWER_CASSETTE_SIZE * 100

        if percent_upper <= PERCENT_NOTIFICATION or percent_lower <= PERCENT_NOTIFICATION:
            text = (
                "<b>⚠️ Заканчиваются купюры в кюпюрдиспенсере!</b>\n\n"
                f"<b>Текущий верхний уровень:</b> {upper_box_count}\n"
                f"<b>Максимальный верхний уровень:</b> {cash_system_settings.UPPER_CASSETTE_SIZE}\n"
                f"<b>Остаток верхнего бокса:</b> {percent_upper:.1f}%\n"
                f"<b>Текущий нижний уровень:</b> {lower_box_count}\n"
                f"<b>Максимальный нижний уровень:</b> {cash_system_settings.LOWER_CASSETTE_SIZE}\n"
                f"<b>Остаток нижнего бокса:</b> {percent_lower:.1f}%"
            )
            await send_to_channel(text)


asyncio.create_task(check_bill_acceptor())
asyncio.create_task(check_bill_dispenser())
