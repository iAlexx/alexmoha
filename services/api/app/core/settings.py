import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_env: str = os.getenv('APP_ENV', 'dev')

    # Required runtime secrets/config for VPS deploy (with backward-compatible fallbacks)
    bot_token: str | None = os.getenv('BOT_TOKEN')
    admin_id: str | None = os.getenv('ADMIN_ID')
    ai_token: str | None = os.getenv('AI_TOKEN') or os.getenv('OPENAI_API_KEY')
    db_url: str = os.getenv('DB_URL', os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/finintel'))

    redis_url: str = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    celery_broker_url: str = os.getenv('CELERY_BROKER_URL', os.getenv('REDIS_URL', 'redis://localhost:6379/0'))
    llm_provider: str = os.getenv('LLM_PROVIDER', 'openai').lower()
    llm_system_prompt: str = os.getenv(
        'LLM_SYSTEM_PROMPT',
        'You are FinIntel AI. Write concise, market-aware, factual updates with clear risk notes in Arabic and English.',
    )
    primary_news_api: str = os.getenv('PRIMARY_NEWS_API', 'https://primary-news.local/feed')
    backup_news_api: str = os.getenv('BACKUP_NEWS_API', 'https://backup-news.local/feed')
    developer_alert_webhook: str | None = os.getenv('DEVELOPER_ALERT_WEBHOOK')
    telegram_webapp_url: str = os.getenv('TELEGRAM_WEBAPP_URL', 'https://app.finintel.local/telegram-webapp')


settings = Settings()
