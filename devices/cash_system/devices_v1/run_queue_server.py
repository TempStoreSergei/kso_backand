import asyncio

from redis.asyncio import Redis
import json

from configs import REDIS_PORT, REDIS_HOST
from payment_system_api import PaymentSystemAPI
from loggers import logger
from payment_system_cash_commands import payment_system_cash_commands


async def listen_to_redis(redis, api):
    """Подключение к Redis и обработка команд"""
    try:
        await api.init_devices()
    except Exception as e:
        logger.error(f"Critical error: {e}")
        await api.shutdown()
        return

    pubsub = redis.pubsub()

    # Подписка на канал команд
    channel = 'payment_system_cash_commands'
    channel_response = f'{channel}_response'
    pubsub.subscribe(channel)
    logger.info("Ожидание команд...")

    # Слушаем канал и выполняем команды
    async for message in pubsub.listen():
        if message.get('type') == 'message':
            raw_data = message.get("data")

            # обработка пинга
            if raw_data == "ping":
                continue
            try:
                command = json.loads(raw_data)
                logger.info(f"Получена команда: {command}")

                # зависит от выбранного устройства
                response = {}
                cash_device = await redis.get('cash_preset_name')
                if cash_device == 'standart':
                    response = await payment_system_cash_commands(command, api)

                await redis.publish(channel_response, json.dumps(response))
                logger.info(f"[{channel}] Ответ отправлен в {channel_response}: {response}")
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка парсинга команды: {e}")
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    payment_api = PaymentSystemAPI(redis)
    asyncio.run(listen_to_redis(redis, payment_api))
