import httpx

from api.configs.loggers import logger
from api.dependencies.redis_connection import get_redis


async def send_to_channel(text: str):
    async for redis in get_redis():
        token = await redis.get('tg_bot_notifications:token')
        chat_id = await redis.get('tg_bot_notifications:chat_id')

        if not token and chat_id:
            return

        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url,
                    json={
                        "chat_id": chat_id,
                        "text": text,
                        "parse_mode": "HTML"
                    }
                )
                return response.json()
        except Exception as e:
            logger.error(f'Не удалось отправить уведомление в телеграмм, ошибка: {e}')
