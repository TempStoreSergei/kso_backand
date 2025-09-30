import base64

from modules.websocket.ws_dto import WSItemDataDTO
from modules.websocket.ws_manager import ws_manager
from modules.scanner.send_scanned_code_dto import SendScannedCodeRequestDTO, \
    SendScannedCodeResponseDTO


async def send_scanned_code(scanned_data: SendScannedCodeRequestDTO):
    encoded = scanned_data.scanned_code
    decoded = base64.b64decode(encoded).decode("utf-8")

    item_data = WSItemDataDTO(
        name='test_product'
    )
    await ws_manager.send_item(item_data)
    print(f"Полученный код после декодирования: {repr(decoded)}")
    return SendScannedCodeResponseDTO(detail='Код отправлен')
