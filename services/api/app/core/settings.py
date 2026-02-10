import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_env: str = os.getenv('APP_ENV', 'dev')
    redis_url: str = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    database_url: str = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/finintel')
    llm_api_key: str | None = os.getenv('OPENAI_API_KEY')
    llm_system_prompt: str = os.getenv(
        'LLM_SYSTEM_PROMPT',
        'You are FinIntel AI. Write concise, market-aware, factual updates with clear risk notes in Arabic and English.',
    )
    primary_news_api: str = os.getenv('PRIMARY_NEWS_API', 'https://primary-news.local/feed')
    backup_news_api: str = os.getenv('BACKUP_NEWS_API', 'https://backup-news.local/feed')
    developer_alert_webhook: str | None = os.getenv('DEVELOPER_ALERT_WEBHOOK')


settings = Settings()
