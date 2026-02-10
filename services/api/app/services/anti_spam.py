from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone


class AntiSpamService:
    def __init__(self, max_requests: int = 10, window_seconds: int = 30) -> None:
        self.max_requests = max_requests
        self.window = timedelta(seconds=window_seconds)
        self.requests: dict[str, deque[datetime]] = defaultdict(deque)

    def allow(self, actor_id: str) -> bool:
        now = datetime.now(timezone.utc)
        q = self.requests[actor_id]

        while q and now - q[0] > self.window:
            q.popleft()

        if len(q) >= self.max_requests:
            return False

        q.append(now)
        return True


anti_spam_service = AntiSpamService()
