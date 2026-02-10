from app.schemas.advanced_analysis import HeatmapItem


class AdvancedAnalysisService:
    @staticmethod
    def smart_heatmap() -> tuple[list[HeatmapItem], list[HeatmapItem]]:
        strongest = [
            HeatmapItem(symbol='BTCUSD', change_pct=2.6, momentum_score=0.88),
            HeatmapItem(symbol='XAUUSD', change_pct=1.4, momentum_score=0.74),
            HeatmapItem(symbol='EURUSD', change_pct=0.9, momentum_score=0.63),
        ]
        weakest = [
            HeatmapItem(symbol='ETHUSD', change_pct=-1.8, momentum_score=0.61),
            HeatmapItem(symbol='GBPUSD', change_pct=-0.7, momentum_score=0.49),
            HeatmapItem(symbol='SOLUSD', change_pct=-2.2, momentum_score=0.77),
        ]
        return strongest, weakest

    @staticmethod
    def divergence(symbol: str, news_impact_score: int, price_move_pct: float) -> tuple[bool, str]:
        divergence = news_impact_score >= 8 and abs(price_move_pct) < 0.2
        msg = f'{symbol}: divergence detected between high-impact news and weak price response' if divergence else f'{symbol}: no major divergence'
        return divergence, msg

    @staticmethod
    def instant_backtest(symbol: str, event_type: str) -> tuple[str, float]:
        return f'https://charts.finintel.local/backtest/{symbol}/{event_type}', 42.0

    @staticmethod
    def liquidity_level(symbol: str, current_price: float, major_level: float) -> tuple[bool, float, str]:
        distance = abs(current_price - major_level) / major_level * 100 if major_level else 0
        near = distance <= 0.4
        msg = f'{symbol} near major liquidity level' if near else f'{symbol} is not near a major liquidity level'
        return near, round(distance, 3), msg
