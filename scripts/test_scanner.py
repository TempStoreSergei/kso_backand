import base64
import httpx

API_URL = "http://localhost:8005/api/v1/scanner/send_scanned_code"
s = "hello" + chr(29) + "world"

encoded = base64.b64encode(s.encode("utf-8")).decode("utf-8")

resp = httpx.post(API_URL, json={"scanned_code": encoded})
print("Отправили:", encoded)
print("Ответ сервера:", resp.status_code, resp.text)