import os

from celery import Celery

broker_url = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672//")
backend_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("finintel_worker", broker=broker_url, backend=backend_url)
celery_app.conf.update(task_serializer="json", result_serializer="json", accept_content=["json"])


@celery_app.task(name="dispatch.telegram")
def dispatch_telegram(payload: dict) -> dict:
    # Placeholder for Telegram fan-out logic with anti-flood throttling.
    return {"status": "queued", "recipients": payload.get("recipients", 0)}


@celery_app.task(name="audio.flash")
def audio_flash(payload: dict) -> dict:
    # Placeholder for VIP+ TTS generation and push.
    return {"status": "generated", "language": payload.get("lang", "ar")}
