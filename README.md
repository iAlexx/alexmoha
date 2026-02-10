# Ultimate Financial Intelligence Bot

منصة ذكاء مالي متكاملة لمراقبة أسواق **Forex** و **Crypto** مع توزيع تنبيهات دقيقة على Telegram + لوحة تحكم ويب.

## What is included now

This repository now provides an **advanced MVP foundation** for the requested system:

- **Hybrid data stack**: PostgreSQL + Redis + Vector DB (Qdrant).
- **Async at scale**: Celery + RabbitMQ for fan-out messaging.
- **Bilingual API contracts**: Arabic/English models for critical outputs.
- **AI pipeline skeleton**: semantic de-duplication + sentiment + impact scoring.
- **Market intelligence endpoints**: correlation radar + whale detector.
- **Growth endpoints**: referral summary + reward rules.
- **Admin controls**: maintenance mode and emergency pause.
- **API anti-spam guard**: request window throttling per client.

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
- `POST /v1/market/correlation-radar`
- `POST /v1/market/whale-detector`
- `GET /v1/growth/referrals/{user_id}`
- `GET/PUT /v1/growth/referral-rules`
- `GET/PATCH /v1/admin/runtime-flags`

## Finalization roadmap (to reach fully production)

1. Integrate real market/news feeds and normalize symbols/timestamps.
2. Replace heuristic AI with embeddings + LLM inference + evaluation harness.
3. Implement persistent DB models/migrations and robust auth/RBAC.
4. Build Telegram template engine + channel operator toolkit.
5. Add full web dashboard (operations room, template builder, finance analytics).
