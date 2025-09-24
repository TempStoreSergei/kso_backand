import time

import httpx

from config import LOKI_URL


def send_loki(level: str, message: str):
    try:
        log_entry = {
            "streams": [
                {
                    "stream": {"level": level, "app": "sb_pay"},
                    "values": [[str(int(time.time() * 1e9)), message]],
                }
            ]
        }
        headers = {"Content-Type": "application/json"}
        with httpx.Client() as client:
            client.post(LOKI_URL, json=log_entry, headers=headers, timeout=2.0)
    except Exception as e:
        print(f"[send_loki error]: {e}")
