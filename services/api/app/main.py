from fastapi import FastAPI

from app.routers.alerts import router as alerts_router
from app.routers.health import router as health_router
from app.routers.news import router as news_router

app = FastAPI(
    title="Ultimate Financial Intelligence API",
    description="Core API for financial news intelligence and alert routing.",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(news_router, prefix="/v1/news", tags=["news"])
app.include_router(alerts_router, prefix="/v1/alerts", tags=["alerts"])
