class PsychologyService:
    @staticmethod
    def calm_alert(symbol: str, volatility_index: float) -> tuple[bool, str]:
        trigger = volatility_index >= 75
        msg = (
            f'🧘 {symbol}: high volatility detected. Avoid FOMO and reduce position size.'
            if trigger
            else f'{symbol}: volatility within manageable range.'
        )
        return trigger, msg
