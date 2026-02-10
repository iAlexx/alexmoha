import hashlib
from dataclasses import dataclass


@dataclass
class SemanticResult:
    dedup_group_id: str
    sentiment: str
    impact_score: int


class AIEngine:
    """Skeleton AI engine for semantic deduplication + sentiment + impact scoring."""

    @staticmethod
    def analyze(title: str, body: str) -> SemanticResult:
        text = f"{title}\n{body}".strip().lower()
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

        negative_keywords = {"drop", "crash", "war", "inflation", "selloff"}
        positive_keywords = {"rise", "surge", "beat", "growth", "rally"}

        score = 5
        sentiment = "neutral"

        if any(k in text for k in negative_keywords):
            sentiment = "negative"
            score = 8
        elif any(k in text for k in positive_keywords):
            sentiment = "positive"
            score = 7

        if "urgent" in text or "breaking" in text:
            score = min(score + 2, 10)

        return SemanticResult(dedup_group_id=digest, sentiment=sentiment, impact_score=score)

    @staticmethod
    def answer_question(question: str, lang: str) -> tuple[str, float]:
        if lang == "ar":
            answer = (
                "التأثير المتوقع يعتمد على سيولة السوق، اتجاه العائدات، وحجم المفاجأة في الخبر. "
                "يفضل تأكيد الإشارة مع حركة السعر والارتباطات قبل الدخول."
            )
        else:
            answer = (
                "Expected impact depends on liquidity, yield direction, and the news surprise magnitude. "
                "Confirm with price action and cross-asset correlations before entering."
            )
        return answer, 0.74
