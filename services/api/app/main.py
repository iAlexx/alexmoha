from fastapi import FastAPI

from app.routers.admin import router as admin_router
from app.routers.advanced_analysis import router as advanced_analysis_router
from app.routers.alerts import router as alerts_router
from app.routers.coach import router as coach_router
from app.routers.digest import router as digest_router
from app.routers.editor import router as editor_router
from app.routers.excellence import router as excellence_router
from app.routers.growth import router as growth_router
from app.routers.health import router as health_router
from app.routers.infra import router as infra_router
from app.routers.integration import router as integration_router
from app.routers.intelligence import router as intelligence_router
from app.routers.market import router as market_router
from app.routers.ops import router as ops_router
from app.routers.news import router as news_router
from app.routers.psychology import router as psychology_router
from app.routers.social import router as social_router
from app.routers.uiux import router as uiux_router
from app.routers.voice import router as voice_router

app = FastAPI(
    title='Ultimate Financial Intelligence API',
    description='Core API for financial news intelligence and alert routing.',
    version='0.4.0',
)

app.include_router(health_router)
app.include_router(news_router, prefix='/v1/news', tags=['news'])
app.include_router(alerts_router, prefix='/v1/alerts', tags=['alerts'])
app.include_router(market_router, prefix='/v1/market', tags=['market'])
app.include_router(growth_router, prefix='/v1/growth', tags=['growth'])
app.include_router(admin_router, prefix='/v1/admin', tags=['admin'])
app.include_router(intelligence_router, prefix='/v1/intelligence', tags=['intelligence'])
app.include_router(integration_router, prefix='/v1/integration', tags=['integration'])
app.include_router(social_router, prefix='/v1/social', tags=['social'])
app.include_router(editor_router, prefix='/v1/editor', tags=['editor'])
app.include_router(excellence_router, prefix='/v1/excellence', tags=['excellence'])
app.include_router(ops_router, prefix='/v1/ops', tags=['ops'])
app.include_router(voice_router, prefix='/v1/voice', tags=['voice'])
app.include_router(digest_router, prefix='/v1/digest', tags=['digest'])
app.include_router(advanced_analysis_router, prefix='/v1/analysis', tags=['analysis'])
app.include_router(coach_router, prefix='/v1/coach', tags=['coach'])
app.include_router(psychology_router, prefix='/v1/psychology', tags=['psychology'])
app.include_router(uiux_router, prefix='/v1/uiux', tags=['uiux'])
app.include_router(infra_router, prefix='/v1/infra', tags=['infra'])
