import os

from celery import Celery

broker_url = os.getenv('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672//')
backend_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

celery_app = Celery('finintel_worker', broker=broker_url, backend=backend_url)
celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    task_acks_late=True,
    worker_prefetch_multiplier=1,
)


@celery_app.task(name='dispatch.telegram')
def dispatch_telegram(payload: dict) -> dict:
    return {'status': 'queued', 'recipients': payload.get('recipients', 0), 'queue': 'telegram'}


@celery_app.task(name='audio.flash')
def audio_flash(payload: dict) -> dict:
    return {'status': 'generated', 'language': payload.get('lang', 'ar'), 'queue': 'tts'}


@celery_app.task(name='session.master.report')
def session_master_report(payload: dict) -> dict:
    return {'status': 'scheduled', 'session': payload.get('session'), 'lead_minutes': 15}


@celery_app.task(name='infographic.render')
def infographic_render(payload: dict) -> dict:
    return {'status': 'rendered', 'image_id': payload.get('image_id'), 'queue': 'media'}


@celery_app.task(name='webhook.fanout')
def webhook_fanout(payload: dict) -> dict:
    return {'status': 'delivered', 'targets': len(payload.get('targets', [])), 'queue': 'webhook'}


@celery_app.task(name='editor.auto')
def editor_auto(payload: dict) -> dict:
    return {'status': 'edited', 'provider': payload.get('provider', 'openai'), 'queue': 'ai_editor'}


@celery_app.task(name='digest.daily')
def digest_daily(payload: dict) -> dict:
    return {'status': 'generated', 'date': payload.get('date'), 'queue': 'digest'}


@celery_app.task(name='heatmap.generate')
def heatmap_generate(payload: dict) -> dict:
    return {'status': 'generated', 'window_h': payload.get('window_h', 4), 'queue': 'analysis'}


@celery_app.task(name='voice.stt')
def voice_stt(payload: dict) -> dict:
    return {'status': 'transcribed', 'audio_url': payload.get('audio_url'), 'queue': 'voice'}
