import os
from math import ceil

from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', os.getenv('REDIS_URL', 'redis://localhost:6379/0'))
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
    recipients = payload.get('recipient_ids', [])
    total = len(recipients)
    per_second = 30
    total_batches = ceil(total / per_second) if total else 0
    batches = [
        recipients[idx: idx + per_second]
        for idx in range(0, total, per_second)
    ]
    return {
        'status': 'queued',
        'recipients': total,
        'queue': 'telegram',
        'rate_limit_per_second': per_second,
        'estimated_seconds': total_batches,
        'batches': total_batches,
        'batch_sizes': [len(batch) for batch in batches],
    }


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


@celery_app.task(name='accuracy.report')
def accuracy_report(payload: dict) -> dict:
    return {'status': 'computed', 'event_id': payload.get('event_id'), 'queue': 'analytics'}


@celery_app.task(name='channel.growth.report')
def channel_growth_report(payload: dict) -> dict:
    return {'status': 'generated', 'channel_id': payload.get('channel_id'), 'queue': 'analytics'}


@celery_app.task(name='post.market.insights')
def post_market_insights(payload: dict) -> dict:
    return {'status': 'generated', 'date': payload.get('date'), 'queue': 'analytics'}
