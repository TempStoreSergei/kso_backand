import base64

from modules.scanner.send_scanned_code_dto import SendScannedCodeRequestDTO, \
    SendScannedCodeResponseDTO


async def send_scanned_code(scanned_data: SendScannedCodeRequestDTO):
    encoded = scanned_data.scanned_code
    decoded = base64.b64decode(encoded).decode("utf-8")

    print(f"Полученный код после декодирования: {repr(decoded)}")
    return SendScannedCodeResponseDTO(detail='Код отправлен')
