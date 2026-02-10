import os
import time

import httpx

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
API_BASE = os.getenv('INTERNAL_API_URL', 'http://api:8000')


def notify_admin(text: str) -> None:
    if not BOT_TOKEN or not ADMIN_ID:
        return
    endpoint = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    try:
        with httpx.Client(timeout=3.0) as client:
            client.post(endpoint, json={'chat_id': ADMIN_ID, 'text': text}).raise_for_status()
    except Exception:
        pass


def run() -> None:
    notify_admin('✅ FinIntel bot service is online.')
    while True:
        try:
            with httpx.Client(timeout=3.0) as client:
                client.get(f'{API_BASE}/health').raise_for_status()
        except Exception as exc:
            notify_admin(f'🚨 Bot cannot reach API service: {exc}')
        time.sleep(60)


if __name__ == '__main__':
    run()
