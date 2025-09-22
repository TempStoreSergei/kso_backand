import asyncio

from redis.asyncio import Redis
import json

from config import REDIS_PORT, REDIS_HOST
from loggers import logger
from command_pinpad_channel_p12 import command_pinpad_channel_p12


async def listen_to_redis():
    """Подключение к Redis и обработка команд"""
    redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    pubsub = redis.pubsub()

    # Подписываемся сразу на все каналы
    await pubsub.subscribe('command_pinpad_channel')
    logger.info("Ожидание команд")

    async for message in pubsub.listen():
        if message.get("type") == "message":
            channel = message.get("channel")
            raw_data = message.get("data")

            # обработка пинга
            if raw_data == "ping":
                continue

            try:
                command = json.loads(raw_data)
                logger.info(f"Получена команда: {command}")

                response = await command_pinpad_channel_p12(command)

                channel_response = f"{channel}_response"
                await redis.publish(channel_response, json.dumps(response))
                logger.info(f"[{channel}] Ответ отправлен в {channel_response}: {response}")

            except json.JSONDecodeError as e:
                logger.error(f"[{channel}] Ошибка парсинга команды: {e}")
            except Exception as e:
                logger.error(f"[{channel}] Неожиданная ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(listen_to_redis())
