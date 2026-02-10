import hashlib

from app.schemas.integration import (
    InfographicGenerateResponse,
    WebhookProvisionResponse,
    WhiteLabelTenantResponse,
)


class IntegrationService:
    @staticmethod
    def provision_webhook(user_id: str, tier: str) -> WebhookProvisionResponse:
        if tier.upper() != 'VIP+':
            return WebhookProvisionResponse(enabled=False, reason='Webhook access requires VIP+')

        token = hashlib.sha256(user_id.encode('utf-8')).hexdigest()[:24]
        return WebhookProvisionResponse(
            enabled=True,
            webhook_url=f'https://hooks.finintel.local/v1/inbound/{token}',
        )

    @staticmethod
    def white_label_enable(tenant_name: str) -> WhiteLabelTenantResponse:
        theme_id = hashlib.md5(tenant_name.encode('utf-8')).hexdigest()[:10]
        return WhiteLabelTenantResponse(tenant_name=tenant_name, enabled=True, theme_id=theme_id)

    @staticmethod
    def generate_infographic(headline: str, symbol: str, bot_link: str) -> InfographicGenerateResponse:
        image_id = hashlib.sha1(f'{headline}:{symbol}'.encode('utf-8')).hexdigest()[:12]
        caption = f'{headline} | {symbol}\nMore on bot: {bot_link}'
        return InfographicGenerateResponse(image_id=image_id, share_caption=caption, render_eta_ms=450)
