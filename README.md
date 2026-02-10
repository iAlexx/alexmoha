# Ultimate Financial Intelligence Bot

منصة ذكاء مالي متكاملة لمراقبة أسواق **Forex** و **Crypto** مع توزيع تنبيهات دقيقة على Telegram + لوحة تحكم ويب.

## What is included in this starter

This repository provides a production-oriented foundation for the requested system:

- **Hybrid data stack**: PostgreSQL + Redis + Vector DB (Qdrant).
- **Async at scale**: Celery + RabbitMQ for fan-out messaging.
- **Bilingual-ready API**: Arabic/English response model.
- **AI pipeline skeleton**: semantic de-duplication + sentiment + impact scoring.
- **Tier-ready product model**: Basic / VIP / VIP+.
- **Admin operations hooks**: maintenance mode + emergency stop flags.

## Architecture (high level)

```text
[News Connectors] -> [Ingestion Service] -> [Dedup + Sentiment + Impact]
                                         -> [PostgreSQL]
                                         -> [Qdrant embeddings]
                                         -> [Celery Queue]
                                                    |
                                                    v
                                            [Telegram Dispatcher]
                                                    |
                                                    v
                                                [Users]

[Web Admin] <-> [API Service] <-> [PostgreSQL/Redis]
```

## Quick start

```bash
docker compose up --build
```

Services:

- API: http://localhost:8000
- RabbitMQ UI: http://localhost:15672 (guest/guest)
- Qdrant: http://localhost:6333

## Key endpoints

- `GET /health`
- `POST /v1/news/ingest`
- `POST /v1/news/ask`
- `POST /v1/alerts/economic-calendar`

## Next implementation milestones

1. Integrate real news feeds (RSS, premium APIs, on-chain sources).
2. Add multilingual template builder for Telegram messages.
3. Connect TTS provider for VIP+ audio flashes.
4. Implement referral leaderboard and affiliate payouts.
5. Add full admin dashboard (React/Next.js).
