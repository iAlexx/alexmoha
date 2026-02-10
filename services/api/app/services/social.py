from collections import defaultdict

from app.schemas.social import SentimentVoteResponse, WhaleWatchResponse


class SocialService:
    def __init__(self) -> None:
        self._votes: dict[str, dict[str, int]] = defaultdict(lambda: {'bullish': 0, 'bearish': 0})

    def vote(self, news_id: str, vote: str) -> SentimentVoteResponse:
        self._votes[news_id][vote] += 1
        bullish = self._votes[news_id]['bullish']
        bearish = self._votes[news_id]['bearish']

        if bullish == bearish:
            bias = 'neutral'
        elif bullish > bearish:
            bias = 'bullish'
        else:
            bias = 'bearish'

        return SentimentVoteResponse(news_id=news_id, bullish=bullish, bearish=bearish, community_bias=bias)

    @staticmethod
    def whale_watch(asset: str, transfer_usd: float, related_news_id: str | None) -> WhaleWatchResponse:
        if transfer_usd >= 25_000_000:
            level = 'critical'
        elif transfer_usd >= 10_000_000:
            level = 'alert'
        elif transfer_usd >= 5_000_000:
            level = 'watch'
        else:
            level = 'info'

        triggered = level in {'alert', 'critical'}
        relation = f'Linked to news {related_news_id}' if related_news_id else 'No active related news context'
        return WhaleWatchResponse(triggered=triggered, level=level, relation_note=relation)


social_service = SocialService()
