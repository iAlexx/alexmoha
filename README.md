# Ultimate Financial Intelligence Bot

منصة ذكاء مالي متكاملة لمراقبة أسواق **Forex** و **Crypto** مع توزيع تنبيهات دقيقة على Telegram + لوحة تحكم ويب.

## What is included now

This repository now provides an **advanced MVP foundation**:

- Hybrid stack: PostgreSQL + Redis + RabbitMQ/Celery + Qdrant.
- Bilingual API contracts (AR/EN) for alerts and AI responses.
- AI workflows: ingestion dedup/sentiment/impact + Ask News.
- Proactive intelligence: session master, gap detector, noise filter.
- VIP+ analytics: backtest-news and fake-news validation gate.
- Market systems: correlation radar + whale detector + whale watch.
- Growth systems: referrals, points, auto VIP rewards, leaderboard.
- Integrations: VIP+ webhook provisioning, infographic generation.
- Admin controls: maintenance mode, emergency pause, white-label tenants.

## Quick start

```bash
docker compose up --build
```

## Key endpoints

- Health: `GET /health`
- News: `POST /v1/news/ingest`, `POST /v1/news/ask`
- Alerts: `POST /v1/alerts/economic-calendar`
- Intelligence:
  - `POST /v1/intelligence/session-master`
  - `POST /v1/intelligence/gap-detector`
  - `POST /v1/intelligence/noise-filter`
  - `POST /v1/intelligence/vip/backtest-news`
  - `POST /v1/intelligence/vip/fake-news-check`
- Market:
  - `POST /v1/market/correlation-radar`
  - `POST /v1/market/whale-detector`
- Social:
  - `POST /v1/social/sentiment-vote`
  - `POST /v1/social/whale-watch`
- Growth:
  - `GET /v1/growth/referrals/{user_id}`
  - `GET/PUT /v1/growth/referral-rules`
  - `GET /v1/growth/leaderboard`
- Integrations:
  - `POST /v1/integration/webhook/provision`
  - `POST /v1/integration/infographic/generate`
  - `POST /v1/integration/white-label/tenant`
- Admin: `GET/PATCH /v1/admin/runtime-flags`

## Performance note

Heavy operations (broadcast, TTS, scheduled reports, webhook fanout, infographic rendering) are designed to run through Celery queues to protect API latency and message delivery throughput.

## Finalization roadmap

1. Persistent DB models/migrations and RBAC/auth.
2. Real providers: market feeds, on-chain data, Telegram API, TTS, LLM.
3. Full web admin dashboard with operations room and template builder.
4. Observability (metrics/tracing), autoscaling, and DR runbooks.
