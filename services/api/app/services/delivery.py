from math import ceil


class DeliveryService:
    TELEGRAM_MAX_PER_SECOND = 30

    @classmethod
    def dispatch_plan(cls, recipients: int) -> dict:
        seconds_required = ceil(recipients / cls.TELEGRAM_MAX_PER_SECOND) if recipients > 0 else 0
        return {
            'recipients': recipients,
            'max_per_second': cls.TELEGRAM_MAX_PER_SECOND,
            'estimated_seconds': seconds_required,
            'strategy': 'token-safe-batched-dispatch',
        }
