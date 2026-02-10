from collections import defaultdict


class OpsService:
    def __init__(self) -> None:
        self._noise_profiles: dict[str, dict] = defaultdict(lambda: {'min_move_pct_5m': 0.5, 'critical_mode': False})

    def set_noise_profile(self, user_id: str, min_move_pct_5m: float, critical_mode: bool) -> dict:
        self._noise_profiles[user_id] = {
            'min_move_pct_5m': min_move_pct_5m,
            'critical_mode': critical_mode,
        }
        return self._noise_profiles[user_id]

    def alert_eligibility(self, user_id: str, move_pct_5m: float, trend_changer: bool) -> tuple[bool, str]:
        profile = self._noise_profiles[user_id]
        if profile['critical_mode'] and not trend_changer:
            return False, 'critical_mode_enabled_only_trend_changers_allowed'
        if abs(move_pct_5m) < profile['min_move_pct_5m']:
            return False, 'below_user_minimum_movement_threshold'
        return True, 'eligible'

    @staticmethod
    def post_market_insight(date: str, headlines: list[str]) -> tuple[str, list[str]]:
        title = f'Post-Market AI Insights — {date}'
        sample = headlines[:5]
        insights = [
            f"Market learned: {h}" for h in sample
        ]
        if not insights:
            insights = ['No major headlines recorded for this session.']
        insights.append('Watch next session liquidity transitions and macro spillover effects.')
        return title, insights

    @staticmethod
    def telegram_webapp_config() -> dict:
        return {
            'enabled': True,
            'webapp_url': 'https://app.finintel.local/telegram-webapp',
            'features': ['preferences', 'watchlist', 'tier', 'alerts'],
        }


ops_service = OpsService()
