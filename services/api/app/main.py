from fastapi import FastAPI

from app.routers.admin import router as admin_router
from app.routers.alerts import router as alerts_router
from app.routers.growth import router as growth_router
from app.routers.health import router as health_router
from app.routers.market import router as market_router
from app.routers.news import router as news_router

app = FastAPI(
    title='Ultimate Financial Intelligence API',
    description='Core API for financial news intelligence and alert routing.',
    version='0.2.0',
)

app.include_router(health_router)
app.include_router(news_router, prefix='/v1/news', tags=['news'])
app.include_router(alerts_router, prefix='/v1/alerts', tags=['alerts'])
app.include_router(market_router, prefix='/v1/market', tags=['market'])
app.include_router(growth_router, prefix='/v1/growth', tags=['growth'])
app.include_router(admin_router, prefix='/v1/admin', tags=['admin'])
