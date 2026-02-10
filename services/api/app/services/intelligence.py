from app.schemas.intelligence import (
    BacktestNewsResponse,
    FakeNewsCheckResponse,
    GapDetectorResponse,
    SessionLiquidityPair,
    SessionMasterResponse,
)


class ProactiveIntelligenceService:
    _session_pairs: dict[str, list[tuple[str, float, str]]] = {
        'london': [
            ('EURUSD', 0.82, 'European macro releases and open liquidity overlap'),
            ('GBPUSD', 0.79, 'UK open volatility and index flow'),
            ('XAUUSD', 0.74, 'Risk sentiment and USD repricing'),
        ],
        'new_york': [
            ('XAUUSD', 0.86, 'US yields and dollar repricing'),
            ('USDJPY', 0.77, 'Treasury-led momentum'),
            ('NAS100', 0.81, 'US cash open expansion'),
        ],
        'tokyo': [
            ('USDJPY', 0.84, 'JPY liquidity concentration in Asia'),
            ('AUDUSD', 0.76, 'Asia risk cycle and commodities'),
            ('NZDUSD', 0.71, 'Regional macro follow-through'),
        ],
    }

    @classmethod
    def session_master(cls, session: str) -> SessionMasterResponse:
        rows = cls._session_pairs.get(session, [])
        top_pairs = [SessionLiquidityPair(symbol=s, expected_volatility=v, reason=r) for s, v, r in rows[:3]]
        avg = sum(v for _, v, _ in rows) / max(len(rows), 1)
        forecast = 'high' if avg >= 0.8 else 'moderate' if avg >= 0.65 else 'low'
        return SessionMasterResponse(session=session, liquidity_forecast=forecast, top_pairs=top_pairs)

    @staticmethod
    def gap_detector(symbol: str, friday_close: float, monday_open: float) -> GapDetectorResponse:
        gap = monday_open - friday_close
        gap_pct = (gap / friday_close) * 100 if friday_close else 0.0
        magnitude = abs(gap_pct)
        close_probability = 0.78 if magnitude <= 0.3 else 0.62 if magnitude <= 0.8 else 0.44
        return GapDetectorResponse(
            symbol=symbol,
            gap_points=round(gap, 5),
            gap_percent=round(gap_pct, 3),
            close_probability=close_probability,
        )


class VipIntelligenceService:
    @staticmethod
    def backtest_news(asset: str, event_type: str, lookback_days: int) -> BacktestNewsResponse:
        # Deterministic synthetic baseline until historical warehouse integration.
        base = max(12, min(lookback_days // 20, 60))
        up = round(base * 1.4, 2)
        down = round(base * 1.1, 2)
        return BacktestNewsResponse(
            asset=asset,
            event_type=event_type,
            avg_up_move_pips=up,
            avg_down_move_pips=down,
            samples=max(16, lookback_days // 9),
        )

    @staticmethod
    def fake_news_detection(trusted_sources_matched: int) -> FakeNewsCheckResponse:
        verified = trusted_sources_matched >= 2
        confidence = 0.9 if trusted_sources_matched >= 3 else 0.72 if verified else 0.38
        note = 'Confirmed by multiple trusted sources' if verified else 'Insufficient source confirmation'
        return FakeNewsCheckResponse(verified_breaking=verified, confidence=confidence, note=note)
