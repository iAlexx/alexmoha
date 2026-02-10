class DailyDigestService:
    @staticmethod
    def build_digest(date: str, headlines: list[str]) -> tuple[str, list[str]]:
        selected = headlines[:6]
        lines = [f"### Daily Digest — {date}", ""]
        lines.extend([f"- {h}" for h in selected])
        lines.append('\n**Focus for tomorrow:** volatility around scheduled macro releases.')
        watch = ['EURUSD around session opens', 'BTCUSD correlation with majors', 'Gold near yield-sensitive levels']
        return '\n'.join(lines), watch
