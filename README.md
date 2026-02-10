# Ultimate Financial Intelligence Bot

منصة ذكاء مالي متكاملة لمراقبة أسواق **Forex** و **Crypto** مع توزيع تنبيهات دقيقة على Telegram + لوحة تحكم ويب.

## Included subsystems

- Core stack: PostgreSQL + Redis + RabbitMQ/Celery + Qdrant.
- News intelligence: ingest/ask + dedup/sentiment/impact.
- Proactive intelligence: session master, gap detector, noise filter.
- AI editor engine: LLM-ready auto-format, financial translation, summarization, admin tone control.
- Historical insight: instant backtest endpoints and historical reaction summaries.
- Voice interaction: STT-ready voice query endpoint.
- Daily Digest AI: end-of-day summarized market digest.
- Flow analytics: smart heatmap, divergence alert, liquidity-level proximity.
- Social/Growth: sentiment votes, whale watch, referrals, points, leaderboard.
- Pro integrations: VIP+ webhook, infographic generator, white-label provisioning.
- AI Trading Coach: VIP+ trading notes + monthly performance report.
- Psychological alerts: calm alerts in extreme volatility.
- UI/UX controls: inline keyboard payload endpoint per news item.

## Key endpoint groups

- `/v1/news`, `/v1/alerts`, `/v1/intelligence`, `/v1/market`
- `/v1/editor`, `/v1/voice`, `/v1/digest`, `/v1/analysis`
- `/v1/coach`, `/v1/psychology`, `/v1/uiux`
- `/v1/growth`, `/v1/social`, `/v1/integration`, `/v1/admin`

## Queue-first performance design

Heavy/async workloads are designed to execute in Celery queues: broadcast, voice/STT, AI editor jobs, daily digest, heatmap generation, webhook fanout, infographic render.

## Quick start

```bash
docker compose up --build
```
