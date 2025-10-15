import asyncio
import base64

from fastapi import HTTPException

from api.db_shop_api.errors import DBShopError
from modules.websocket.ws_dto import WSOrderDataDTO
from modules.websocket.ws_manager import ws_manager
from modules.scanner.send_scanned_code_dto import SendScannedCodeRequestDTO, \
    SendScannedCodeResponseDTO, CheckScannerServiceResponseDTO
from modules.scanner.loggers import logger
from api.db_shop_api.db_shop_client import db_shop_client


async def send_scanned_code(scanned_data: SendScannedCodeRequestDTO):
    encoded = scanned_data.scanned_code
    decoded = base64.b64decode(encoded).decode("utf-8")
    logger.info(f"Полученный код после декодирования: {repr(decoded)}")

    try:
        order = await db_shop_client.get_order(f'ЗаказНаряд:Яр{decoded[1:]}')
        logger.debug(order)
        ws_order_data = WSOrderDataDTO(**order)
        ws_order_data.sum *= 100
        ws_order_data.avance *= 100
        for item in ws_order_data.cart:
            item.price *= 100
            if item.tax == -1:
                item.tax = 0
        await ws_manager.send_order(ws_order_data)
        return SendScannedCodeResponseDTO(detail='Код отправлен')
    except DBShopError as e:
        logger.error(f"Ошибка при получении заказа из 1С: {e}")
        raise HTTPException(e.status_code, e.message)


async def check_scanner_service():
    proc_status = await asyncio.create_subprocess_exec(
        "sudo", "systemctl", "is-active", "scanner.service",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    status_out, _ = await proc_status.communicate()
    status = status_out.decode().strip()

    if status == "active":
        return CheckScannerServiceResponseDTO(
            status=True,
            detail=None,
        )
    return CheckScannerServiceResponseDTO(
        status=False,
        detail='Сервис сканера не запущен',
    )
