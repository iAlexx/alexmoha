from app.schemas.market import CorrelationOpportunity, WhaleDetectionResponse


class MarketIntelligenceService:
    _correlation_map: dict[str, list[str]] = {
        "XAUUSD": ["AUDUSD", "NZDUSD", "USDCHF"],
        "BTCUSD": ["ETHUSD", "SOLUSD"],
        "DXY": ["EURUSD", "GBPUSD", "XAUUSD"],
    }

    @classmethod
    def correlation_radar(cls, trigger_symbol: str, trigger_move_pct: float) -> list[CorrelationOpportunity]:
        related = cls._correlation_map.get(trigger_symbol.upper(), [])
        if not related:
            return []

        direction = "up" if trigger_move_pct > 0 else "down"
        base_conf = min(abs(trigger_move_pct) / 3.0, 0.9)
        return [
            CorrelationOpportunity(symbol=s, expected_direction=direction, confidence=round(max(0.35, base_conf), 2))
            for s in related
        ]

    @staticmethod
    def whale_detector(asset: str, transfer_usd: float, price_spike_pct: float) -> WhaleDetectionResponse:
        score = 0
        if transfer_usd >= 5_000_000:
            score += 2
        if transfer_usd >= 25_000_000:
            score += 2
        if abs(price_spike_pct) >= 3:
            score += 1
        if abs(price_spike_pct) >= 7:
            score += 2

        if score >= 5:
            level = "critical"
        elif score >= 4:
            level = "high"
        elif score >= 2:
            level = "medium"
        else:
            level = "low"

        suspicious = level in {"high", "critical"}
        reason = (
            f"{asset}: transfer=${transfer_usd:,.0f}, spike={price_spike_pct:.2f}%, "
            f"risk={level}"
        )
        return WhaleDetectionResponse(suspicious=suspicious, risk_level=level, reason=reason)
