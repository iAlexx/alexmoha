from collections import defaultdict

from app.schemas.excellence import (
    ChannelGrowthResponse,
    PersonalizationProfileResponse,
    PostEventAccuracyResponse,
    TradeReadinessResponse,
    TrustScoreResponse,
)


class ExcellenceService:
    def __init__(self) -> None:
        self._profiles: dict[str, PersonalizationProfileResponse] = {}
        self._accuracy_log: dict[str, list[float]] = defaultdict(list)

    @staticmethod
    def trust_score(source_reliability: float, source_confirmations: int, freshness_minutes: int, price_alignment: float) -> TrustScoreResponse:
        freshness_component = max(0.0, 1 - (freshness_minutes / 240))
        confirmations_component = min(source_confirmations / 4, 1.0)
        score = (
            source_reliability * 35
            + confirmations_component * 30
            + freshness_component * 20
            + price_alignment * 15
        )
        trust = int(round(min(max(score, 0), 100)))
        band = 'high' if trust >= 75 else 'medium' if trust >= 45 else 'low'
        return TrustScoreResponse(trust_score=trust, confidence_band=band)

    @staticmethod
    def trade_readiness(impact_score: int, liquidity_score: float, volatility_score: float, level_proximity_score: float) -> TradeReadinessResponse:
        readiness = (
            (impact_score / 10) * 4
            + liquidity_score * 2.2
            + volatility_score * 1.8
            + level_proximity_score * 2.0
        )
        readiness = round(min(max(readiness, 0), 10), 2)
        bias = 'ready' if readiness >= 7.2 else 'monitor' if readiness >= 4.5 else 'wait'
        return TradeReadinessResponse(readiness_score=readiness, action_bias=bias)

    def save_profile(
        self,
        user_id: str,
        symbols: list[str],
        quiet_hours_utc: list[int],
        analysis_mode: str,
        alert_intensity: str,
    ) -> PersonalizationProfileResponse:
        profile = PersonalizationProfileResponse(
            user_id=user_id,
            symbols=symbols,
            quiet_hours_utc=sorted(list(set([h for h in quiet_hours_utc if 0 <= h <= 23]))),
            analysis_mode=analysis_mode,
            alert_intensity=alert_intensity,
        )
        self._profiles[user_id] = profile
        return profile

    def get_profile(self, user_id: str) -> PersonalizationProfileResponse:
        return self._profiles.get(
            user_id,
            PersonalizationProfileResponse(
                user_id=user_id,
                symbols=['EURUSD', 'BTCUSD', 'XAUUSD'],
                quiet_hours_utc=[],
                analysis_mode='hybrid',
                alert_intensity='normal',
            ),
        )

    def post_event_accuracy(
        self,
        event_id: str,
        predicted_direction: str,
        actual_direction: str,
        predicted_move_pips: float,
        actual_move_pips: float,
    ) -> PostEventAccuracyResponse:
        direction_correct = predicted_direction == actual_direction
        if actual_move_pips == 0:
            magnitude_error_pct = 0 if predicted_move_pips == 0 else 100
        else:
            magnitude_error_pct = abs(predicted_move_pips - actual_move_pips) / abs(actual_move_pips) * 100

        base = 65 if direction_correct else 25
        penalty = min(magnitude_error_pct * 0.4, 55)
        accuracy = round(max(0, min(100, base - penalty + 35)), 2)

        self._accuracy_log[event_id].append(accuracy)
        return PostEventAccuracyResponse(
            event_id=event_id,
            direction_correct=direction_correct,
            magnitude_error_pct=round(magnitude_error_pct, 2),
            accuracy_score=accuracy,
        )

    @staticmethod
    def channel_growth(channel_id: str, posts_last_7d: int, reactions_last_7d: int, shares_last_7d: int) -> ChannelGrowthResponse:
        denominator = max(posts_last_7d, 1)
        engagement = round(((reactions_last_7d * 0.7 + shares_last_7d * 1.3) / denominator), 2)

        if engagement >= 40:
            window = '12:00-16:00 UTC'
        elif engagement >= 20:
            window = '08:00-12:00 UTC'
        else:
            window = '16:00-20:00 UTC'

        recommendations = [
            'Increase high-impact macro explainers with concise bullets.',
            'Use infographic cards for key news + CTA link.',
            'Post follow-up reaction update 20-40 min after major release.',
        ]
        return ChannelGrowthResponse(
            channel_id=channel_id,
            engagement_score=engagement,
            best_posting_window_utc=window,
            content_recommendations=recommendations,
        )


excellence_service = ExcellenceService()
