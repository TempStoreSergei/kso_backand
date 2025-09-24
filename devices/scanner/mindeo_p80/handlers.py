import json
from datetime import datetime, timezone

import httpx

from config import DBUrls, APIUrls, FISCAL_DRIVE_NUMBER, MARK_API_KEY, BASE_DB_AUTH, TERMINAL_ID
from humps import camelize
from loggers import logger


async def send_error(client: httpx.AsyncClient, detail: str):
    """Функция отправляет сообщение об ошибке в вебсокет и лог в 1С."""
    await client.post(APIUrls.MESSAGE, json={"event": "errorBasket", "detail": detail})
    await client.post(
        DBUrls.LOG,
        json={
            'event': 'scaner_error',
            'data': detail,
        },
        params={'id': TERMINAL_ID},
        auth=BASE_DB_AUTH,
    )


async def handle_basket(client: httpx.AsyncClient, code: str):
    """Обработчик кода корзины товаров."""
    response = await client.get(
        DBUrls.BASKET,
        params={"qr_code": code, 'id': TERMINAL_ID},
        auth=BASE_DB_AUTH,
    )
    if response.status_code != 200:
        logger.error(f"Не удалось получить корзину товаров: {code}")
        await send_error(client, f"Не удалось получить корзину товаров: {code}")
        return False
    else:
        data = response.json()
        logger.info(f"Получена корзина товаров:\n{data}")
        await client.post(APIUrls.BASKET, json=camelize(data))
        return True


async def handle_client(client: httpx.AsyncClient, code: str):
    """Обработчик кода карты клиента."""
    response = await client.get(
        DBUrls.CLIENT,
        params={"client_qr_code": code, 'id': TERMINAL_ID},
        auth=BASE_DB_AUTH,
    )
    if response.status_code != 200:
        logger.error(f"Не удалось получить клиента: {code}")
        return False
    else:
        data = response.json()
        logger.info(f"Получен клиент:\n{data}")
        await client.post(APIUrls.CLIENT, json=camelize(data.get('client_data')))
        return True


async def handle_fair_mark(client: httpx.AsyncClient, code: str, sdn_hosts: list[str] | None):
    """Обработчик кода честного знака."""
    payload = {
        "fair_mark": code  # code содержит chr(29)
    }
    json_str = json.dumps(payload, ensure_ascii=False)
    json_str = json_str.replace('\\u001d', chr(29))
    response = await client.post(
        DBUrls.FIRE_MARK,
        data=json_str.encode('utf-8'),
        params={'id': TERMINAL_ID},
        auth=BASE_DB_AUTH,
        headers={'Content-Type': 'application/json; charset=utf-8'},
    )
    if response.status_code != 200:
        logger.error(f"Не удалось получить товар: {code}")
        await send_error(client, f"Не удалось получить товар: {code}")
    else:
        item_data = response.json()
        logger.info(f'Получен товар по честному знаку:\n{item_data}')
        # Проверяем валидность честного знака
        code_data = {}
        mark_data = {}
        for host in sdn_hosts:
            try:
                response = await client.post(
                    f'{host}/api/v4/true-api/codes/check',
                    json={'codes': [code], 'fiscalDriveNumber': FISCAL_DRIVE_NUMBER},
                    headers={'X-API-KEY': MARK_API_KEY},
                    timeout=2,
                )
                if response.status_code != 200:
                    logger.error(f'Некорректный запрос кода маркировки: {code}')
                    await send_error(client, f'Некорректный запрос кода маркировки: {code}')
                    continue

                mark_data = response.json()
                if codes_data := mark_data.get('codes', []):
                    code_data = codes_data[0]
                    logger.debug(f'Данные честного знака получены успешно: {code_data}')
                break
            except httpx.TimeoutException:
                logger.error(f'Таймаут запроса к SDN хосту {host}')
                continue
            except httpx.RequestError as e:
                logger.error(f'Ошибка запроса к SDN хосту {host}: {e}')
                continue

        if code_data:
            reasons = []

            if not code_data.get('found'):
                reasons.append('Маркировка не найдена')
            if not code_data.get('valid'):
                reasons.append('Маркировка невалидна')
            if not code_data.get('verified'):
                reasons.append('Маркировка не подтверждена')
            if not code_data.get('realizable'):
                reasons.append('Маркировка не реализуема')

            expire_str = code_data.get('expireDate')
            if expire_str:
                try:
                    expire_date = datetime.fromisoformat(expire_str.replace('Z', '+00:00'))
                    now = datetime.now(timezone.utc)
                    if expire_date <= now:
                        reasons.append('Срок действия маркировки истёк')
                except ValueError:
                    reasons.append('Некорректный формат даты истечения срока')

            if not reasons:
                item_data.get('item_data').update({
                    'req_id': mark_data.get('reqId'),
                    'req_timestamp': mark_data.get('reqTimestamp'),
                    'item_fair_mark_value': code,
                })
                logger.info('Маркировка успешно прошла проверку')
                await client.post(APIUrls.BARCODE, json=camelize(item_data))
            else:
                error_msg = '; '.join(reasons)
                logger.error(f'Код маркировки не прошел проверку: {error_msg}')
                await send_error(client, f'Код маркировки не прошел проверку: {error_msg}')
        else:
            logger.error('Не удалось запросить информацию по коду маркировки')
            await send_error(client, 'Не удалось запросить информацию по коду маркировки')


async def handle_regular_barcode(client: httpx.AsyncClient, code: str):
    """Обработчик кода товара."""
    response = await client.post(
        DBUrls.BARCODE,
        json={"item_baracode": code},
        params={'id': TERMINAL_ID},
        auth=BASE_DB_AUTH,
    )
    if response.status_code != 200:
        logger.error(f"Не удалось получить товар: {code}")
        return None

    data = response.json()
    logger.debug(f"Получены данные баракода:\n{data}")

    fair_mark = data.get("item_data", {}).get("item_fair_mark", None)
    if fair_mark:
        logger.error("Требуется отсканировать qr код честного знака!")
        await client.post(
            APIUrls.MESSAGE,
            json={
                "event": "basketFairMark",
                "detail": "Требуется отсканировать qr код честного знака!",
            },
        )
        return fair_mark
    else:
        logger.info(f"Получен товар:\n{data}")
        return data


async def handle_promo_code(client: httpx.AsyncClient, code: str):
    """Обработчик кода карты клиента."""
    logger.info("Отсканирован промокод")
    response = await client.get(
        DBUrls.PROMO,
        params={"promo": code, 'id': TERMINAL_ID},
        auth=BASE_DB_AUTH,
    )

    if response.status_code != 200:
        logger.error(f"Не удалось получить промокод: {code}")
        await send_error(client, 'Ошибка сканирования')
        await client.post(
            APIUrls.MESSAGE,
            json={
                'event': 'promoError',
                'detail': 'Ошибка получения промокода',
                'data': code,
            },
        )
    else:
        logger.info("Промокод получен успешно")
        await client.post(
            APIUrls.MESSAGE,
            json={
                'event': 'promo',
                'detail': 'Получен промокод',
                'data': code,
            },
        )
