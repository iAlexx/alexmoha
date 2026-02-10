class UIUXService:
    @staticmethod
    def inline_controls(news_id: str) -> list[dict[str, str]]:
        return [
            {'text': '📈 التحليل الفني', 'callback_data': f'tech:{news_id}'},
            {'text': '🧾 التحليل الأساسي', 'callback_data': f'fund:{news_id}'},
            {'text': '📊 الشارت', 'callback_data': f'chart:{news_id}'},
        ]
