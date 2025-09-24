import os

import httpx
from httpx import AsyncClient
import serial.tools.list_ports
from redis.asyncio import Redis
from humps import camelize

from config import APIUrls, MARK_API_KEY, MARK_API_URL
from handlers import handle_fair_mark, handle_regular_barcode, handle_client, handle_basket, \
    handle_promo_code, send_error
from loggers import logger


async def del_item_fire_mark_process(
    barcode: str,
    redis: Redis,
    client: AsyncClient,
    del_item_fire_mark: str,
):
    if barcode == del_item_fire_mark:
        logger.info('Товар для удаления отсканирован успешно')
        await redis.delete('del_item_fire_mark')
        await client.post(
            APIUrls.MESSAGE,
            json={
                "event": "deleteItemSuccess",
                "detail": "Товар удален успешно",
            },
        )
    else:
        data = await handle_regular_barcode(client, barcode)
        if data.get('detail') == 'Это консультант.':
            logger.info('Отсканирована карта консультанта')
            await client.get(APIUrls.CONS)
        else:
            logger.error("Отсканирован неверный код честного знака")


async def only_baskets_process(
    barcode: str,
    redis: Redis,
    client: AsyncClient,
):
    is_basket = await handle_basket(client, barcode)
    if not is_basket:
        data = await handle_regular_barcode(client, barcode)
        if data.get('detail') == 'Это консультант.':
            logger.info('Отсканирована карта консультанта')
            await client.get(APIUrls.CONS)
        else:
            await send_error(client, f"Отсканирован некорректный баракод: {barcode}")
        return
    await redis.delete('only_baskets')


async def default_item_process(
        barcode: str,
        redis: Redis,
        client: AsyncClient,
        sdn_hosts: list[str],
):
    """Функция обрабатывает процесс сканирования товаров в дефолтном состоянии сканера."""
    if barcode.startswith("01"):
        await handle_fair_mark(client, barcode, sdn_hosts)
        await redis.set("item_without_basket", "True")

    else:
        data = await handle_regular_barcode(client, barcode)
        if not data:
            client_data = await handle_client(client, barcode)
            if not client_data:
                await handle_promo_code(client, barcode)
        elif item := data.get("item_data", {}):
            if fair_mark := item.get("item_fair_mark", None):
                logger.error("Требуется отсканировать qr код честного знака!")
                await client.post(
                    APIUrls.MESSAGE,
                    json={
                        "event": "basketFairMark",
                        "detail": "Требуется отсканировать qr код честного знака!",
                    },
                )
                await redis.set("fair_mark", fair_mark)
            else:
                logger.info('Товар отсканирован успешно')
                await client.post(APIUrls.BARCODE, json=camelize(data))
            await redis.set("item_without_basket", "True")

        elif gift_card := data.get("gift_card"):
            logger.info('Отсканирована подарочная карта')
            await client.post(APIUrls.GIFT_CART, json=camelize(gift_card))

        elif data.get('detail') == 'Это консультант.':
            logger.info('Отсканирована карта консультанта')
            await client.get(APIUrls.CONS)


async def item_without_basket_process(
    barcode: str,
    redis: Redis,
    client: AsyncClient,
    sdn_hosts: list[str],
):
    """
    Функция обрабатывает процесс сканирования товаров при условии, что уже отсканирован
    какой-либо товар. В данном процессе заблокирована отправка готовых корзин.
    """
    logger.info('Сканнер в состоянии сканирования отдельных товаров без корзины')
    fair_mark = await redis.get("fair_mark")

    if fair_mark:
        logger.info('Сканнер в ожидании кода ЧЗ')
        if barcode == fair_mark:
            await handle_fair_mark(client, barcode, sdn_hosts)
            await redis.delete("fair_mark")
        elif barcode != fair_mark:
            data = await handle_regular_barcode(client, barcode)
            if not data:
                await handle_client(client, barcode)
            elif data.get('detail') == 'Это консультант.':
                logger.info('Отсканирована карта консультанта')
                await client.get(APIUrls.CONS)
        else:
            logger.error("Отсканирован неверный код честного знака")

    else:
        if barcode.startswith("01"):
            await handle_fair_mark(client, barcode, sdn_hosts)

        else:
            data = await handle_regular_barcode(client, barcode)
            if not data:
                client_data = await handle_client(client, barcode)
                if not client_data:
                    await handle_promo_code(client, barcode)
            elif item := data.get("item_data", {}):
                if item.get("item_fair_mark", None):
                    logger.error("Требуется отсканировать qr код честного знака!")
                    await client.post(
                        APIUrls.MESSAGE,
                        json={
                            "event": "basketFairMark",
                            "detail": "Требуется отсканировать qr код честного знака!",
                        },
                    )
                    await redis.set("fair_mark", fair_mark)
                else:
                    logger.info('Товар отсканирован успешно')
                    await client.post(APIUrls.BARCODE, json=camelize(data))

            elif gift_card := data.get("gift_card"):
                logger.info('Отсканирована подарочная карта')
                await client.post(APIUrls.GIFT_CART, json=camelize(gift_card))

            elif data.get('detail') == 'Это консультант.':
                logger.info('Отсканирована карта консультанта')
                await client.get(APIUrls.CONS)


def find_serial_device(vendor_id: int, product_id: int) -> str | None:
    """
    Ищет COM-порт сканера по VID/PID.
    Возвращает строку с путем, например '/dev/ttyACM0', или None, если не найдено.
    VID 0x1EAB - стандартный для Mindeo. PID может отличаться.
    """
    ports = serial.tools.list_ports.comports()
    logger.debug(f"Поиск среди доступных портов: {[p.device for p in ports]}")

    # 1. Приоритетный поиск по VID (и PID, если указан)
    for port in ports:
        if port.vid == vendor_id and (product_id is None or port.pid == product_id):
            logger.info(f"Найден сканер Mindeo по VID/PID: {port.device} ({port.description})")
            return port.device

    # 2. Резервный поиск по описанию, если по VID/PID не нашлось
    for port in ports:
        desc = port.description.lower()
        if "scanner" in desc or "mindeo" in desc or "barcode" in desc:
            logger.info(f"Найдено COM-устройство по описанию: {port.device} ({port.description})")
            return port.device

    return None


def find_serial_device_by_name(
    name_substring: str = "usb-Linux_3.10.14_with_dwc2-gadget_GadGet_Serial_v2.4-if00"
) -> str | None:
    """
    Ищет COM-порт по части имени в /dev/serial/by-id/.
    Возвращает путь к устройству (например, '/dev/serial/by-id/...') или None, если не найдено.
    """
    search_path = "/dev/serial/by-id/"
    try:
        for entry in os.listdir(search_path):
            if name_substring in entry:
                full_path = os.path.realpath(os.path.join(search_path, entry))
                logger.info(f"Найден порт по имени: {entry} -> {full_path}")
                return full_path
    except FileNotFoundError:
        logger.warning(f"Каталог {search_path} не найден — вероятно, нет подключенных USB-UART устройств.")
    return None


async def get_sdn_hosts():
    """Получение списка хостов cdn для проверки честного знака."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            MARK_API_URL,
            headers={'X-API-KEY': MARK_API_KEY},
        )
        if response.status_code != 200:
            logger.error('Ошибка при получении sdn площадок')
            return None

        sdn_hosts = []
        for item in response.json().get('hosts'):
            sdn_hosts.append(item.get('host'))

        return sdn_hosts
