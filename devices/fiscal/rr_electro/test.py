import asyncio
from asyncio.exceptions import TimeoutError
import json

from redis.asyncio import Redis


async def pubsub_command_util(redis: Redis, channel: str, command: dict):
    """Функция создает подписчика и слушателя Redis."""
    pubsub = redis.pubsub()
    await pubsub.subscribe(f"{channel}_response")

    await redis.publish(channel, json.dumps(command))

    try:
        response_data = await wait_for_response(pubsub)
        return {"code": 200, "detail": "Ответ получен", "data": response_data}
    except TimeoutError:
        return print("Таймаут ожидания ответа от устройства")
    finally:
        await pubsub.unsubscribe(f"{channel}_response")
        await pubsub.close()


async def wait_for_response(pubsub, timeout: int = 15):
    """Ожидание ответа из Redis Pub/Sub с указанным command_id."""
    async def _listener():
        async for message in pubsub.listen():
            if message["type"] == "message":
                try:
                    data = json.loads(message["data"])
                    return data
                except Exception:
                    continue
    return await asyncio.wait_for(_listener(), timeout=timeout)

if __name__ == '__main__':
    redis = Redis(host='localhost', port=6379, decode_responses=True)


    items = [{
                'quantity': 1,
                'price': 100,
                'tax': 0,
                'name': 'tovar1',
            }]
    command_data = {
        "command": "create_check_after_payment",
        "kwargs": {
            'items': items,
            'is_printing': True,
            'payment_method': 1,
            'summ_total': 100,
            'advance_payment': 0
        },
    }

    channel = 'command_fr_channel'
    asyncio.run(pubsub_command_util(redis, channel, command_data))