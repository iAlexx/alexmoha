from pydantic import BaseModel, Field


class WebhookProvisionRequest(BaseModel):
    user_id: str
    tier: str


class WebhookProvisionResponse(BaseModel):
    enabled: bool
    webhook_url: str | None = None
    reason: str | None = None


class WhiteLabelTenantRequest(BaseModel):
    tenant_name: str
    branding_logo_url: str
    bot_link: str


class WhiteLabelTenantResponse(BaseModel):
    tenant_name: str
    enabled: bool
    theme_id: str


class InfographicGenerateRequest(BaseModel):
    headline: str
    summary: str
    symbol: str
    bot_link: str


class InfographicGenerateResponse(BaseModel):
    image_id: str
    image_path: str
    share_caption: str
    render_eta_ms: int = Field(..., ge=0)
