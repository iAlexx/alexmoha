from fastapi import APIRouter

from app.schemas.integration import (
    InfographicGenerateRequest,
    InfographicGenerateResponse,
    WebhookProvisionRequest,
    WebhookProvisionResponse,
    WhiteLabelTenantRequest,
    WhiteLabelTenantResponse,
)
from app.services.integration import IntegrationService

router = APIRouter()


@router.post('/webhook/provision', response_model=WebhookProvisionResponse)
def provision_webhook(payload: WebhookProvisionRequest) -> WebhookProvisionResponse:
    return IntegrationService.provision_webhook(payload.user_id, payload.tier)


@router.post('/white-label/tenant', response_model=WhiteLabelTenantResponse)
def white_label_tenant(payload: WhiteLabelTenantRequest) -> WhiteLabelTenantResponse:
    return IntegrationService.white_label_enable(payload.tenant_name)


@router.post('/infographic/generate', response_model=InfographicGenerateResponse)
def infographic_generate(payload: InfographicGenerateRequest) -> InfographicGenerateResponse:
    return IntegrationService.generate_infographic(payload.headline, payload.symbol, payload.bot_link)
