import httpx

from config import WS_URL


def send_to_ws(event: str, data: dict = None, detail: str = None):
    """
    Отправляет сообщение на эндпоинт /api/v1/baskets/broadcast_message.
    """
    message = {"event": event, "data": data, "detail": detail}

    with httpx.Client() as client:
        response = client.post(WS_URL, json=message)

    print(response)
