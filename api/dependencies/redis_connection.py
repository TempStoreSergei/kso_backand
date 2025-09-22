import asyncio
import json
from functools import wraps
from uuid import uuid4

from fastapi import HTTPException
from redis.asyncio import Redis
from redis.exceptions import ConnectionError, TimeoutError

from api.configs.settings import settings



def handle_redis_errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except TimeoutError as e:
            raise HTTPException(status_code=504, detail=str(e))
        except ConnectionError as e:
            raise HTTPException(500, f'Redis не доступен: {e}')
        except ValueError as e:
            raise HTTPException(status_code=500, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка при работе с Redis: {e}")
    return wrapper


async def get_redis():
    """Получение объекта Redis как зависимость FastAPI."""
    redis = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        decode_responses=True,
    )
    try:
        await redis.ping()
        yield redis
    except ConnectionError as e:
        raise HTTPException(500, f'Redis не доступен: {e}')
    finally:
        await redis.close()


async def pubsub_command_util(redis: Redis, channel: str, command: dict):
    """Функция создает подписчика и слушателя Redis."""
    command["command_id"] = str(uuid4())
    pubsub = redis.pubsub()
    await pubsub.subscribe(f"{channel}_response")

    # Отправляем команду
    await redis.publish(channel, json.dumps(command))

    # Ждём ответ
    response_data = await wait_for_response(pubsub, command["command_id"])
    await pubsub.unsubscribe(f"{channel}_response")

    return response_data


async def wait_for_response(pubsub, command_id, timeout: int = 15):
    """Ожидание ответа из Redis Pub/Sub с проверкой command_id."""
    async def _listener():
        async for message in pubsub.listen():
            if message.get("type") == "message":
                try:
                    data = json.loads(message["data"])
                    if data.get('command_id') == command_id:
                        return data
                except json.JSONDecodeError:
                    raise ValueError(f"Некорректный JSON в сообщении: {message}")

    return await asyncio.wait_for(_listener(), timeout=timeout)
