# Ultimate Financial Intelligence Bot

منصة ذكاء مالي متكاملة لمراقبة أسواق **Forex** و **Crypto** مع توزيع تنبيهات دقيقة على Telegram + لوحة تحكم ويب.

## Included subsystems

- Core stack: PostgreSQL + Redis + RabbitMQ/Celery + Qdrant.
- Async dispatch: Celery with Redis broker support + token-safe batching (30 msg/sec planning).
- News intelligence: ingest/ask + dedup/sentiment/impact.
- Proactive intelligence: session master, gap detector, noise filter.
- AI editor engine: LLM-ready auto-format, financial translation, summarization, admin tone control.
- AI optimization: 10-minute AI output caching + fixed system prompt context.
- Historical insight: instant backtest endpoints and historical reaction summaries.
- Voice interaction: STT-ready voice query endpoint.
- Daily Digest AI: end-of-day summarized market digest.
- Flow analytics: smart heatmap, divergence alert, liquidity-level proximity.
- Social/Growth: sentiment votes, whale watch, referrals, points, leaderboard.
- Pro integrations: VIP+ webhook, infographic generator, white-label provisioning.
- AI Trading Coach: VIP+ trading notes + monthly performance report.
- Psychological alerts: calm alerts in extreme volatility.
- UI/UX controls: inline keyboard payload endpoint per news item.
- Excellence engine: trust score, trade readiness, personalization, post-event accuracy, and channel growth kit.
- Ops/infra maturity: failover source fetching, system health endpoint, anti-noise preferences, critical mode, post-market insights, Telegram WebApp config.
- Advanced DB schema included for users/subscriptions/activity logs.

## Key endpoint groups

- `/v1/news`, `/v1/alerts`, `/v1/intelligence`, `/v1/market`
- `/v1/editor`, `/v1/voice`, `/v1/digest`, `/v1/analysis`, `/v1/excellence`
- `/v1/coach`, `/v1/psychology`, `/v1/uiux`, `/v1/ops`, `/v1/infra`
- `/v1/growth`, `/v1/social`, `/v1/integration`, `/v1/admin`

## Queue-first performance design

Heavy/async workloads execute in Celery queues: broadcast, voice/STT, AI editor jobs, daily digest, heatmap generation, webhook fanout, infographic render, accuracy/growth analytics.

## Environment and secrets

Use environment variables (recommended via `.env`) for keys and endpoints:

- `OPENAI_API_KEY`
- `LLM_SYSTEM_PROMPT`
- `DEVELOPER_ALERT_WEBHOOK`
- `PRIMARY_NEWS_API`
- `BACKUP_NEWS_API`
- `CELERY_BROKER_URL`

## Database schema

Reference SQL schema for users/subscriptions/activity logs:

- `services/api/app/db/schema.sql`

## Quick start

```bash
docker compose up --build
```
