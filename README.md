# Ultimate Financial Intelligence Bot

منصة ذكاء مالي متكاملة لمراقبة أسواق **Forex** و **Crypto** مع تنبيهات Telegram ولوحة WebApp.

## VPS quick deployment

1. انسخ `.env.example` إلى `.env` ثم عبّئ القيم الأساسية:
   - `BOT_TOKEN`
   - `ADMIN_ID`
   - `AI_TOKEN`
   - `DB_URL`
2. شغّل:

```bash
docker compose up -d --build
```

## Core architecture

- API: FastAPI
- Async queues: Celery + Redis
- DB: PostgreSQL
- Bot runtime: `services/bot`
- Daily DB backup service: `backup`

## Key production features

- Centralized env configuration (no code edits required after filling `.env`).
- AI formatter with OpenAI/Gemini support and automatic timeout fallback to raw news.
- Admin access bound to `ADMIN_ID` header (`X-Admin-Id`) and admin dashboard endpoint.
- Immediate admin alerts (Telegram) for technical/API failures and AI quota issues.
- Infographic engine that generates PNG cards for urgent news with caption.
- Advanced broadcasting queue planning with Telegram-safe `30 msg/sec` batching.
- Auto-recovery (`restart: always`) for all core containers.
- Automated daily DB backup to `./backups`.

## Important endpoints

- Health: `GET /health`
- Admin dashboard: `GET /v1/admin/dashboard`
- Runtime flags: `GET/PATCH /v1/admin/runtime-flags`
- AI editor: `POST /v1/editor/format`
- Infographic generation: `POST /v1/integration/infographic/generate`

