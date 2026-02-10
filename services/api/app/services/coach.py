from collections import defaultdict


class CoachService:
    def __init__(self) -> None:
        self.notes: dict[str, list[str]] = defaultdict(list)

    def add_note(self, user_id: str, tier: str, note: str) -> tuple[bool, int]:
        if tier.upper() != 'VIP+':
            return False, len(self.notes[user_id])
        self.notes[user_id].append(note)
        return True, len(self.notes[user_id])

    @staticmethod
    def monthly_report(user_id: str, month: str) -> tuple[list[str], list[str], list[str]]:
        strengths = ['Improved risk control around major news', 'Better session timing discipline']
        mistakes = ['Entering too early before confirmation', 'Overtrading after high volatility spikes']
        plan = ['Wait for 2-step confirmation', 'Cap trades after 2 losses/day', f'Review {month} event journal weekly']
        return strengths, mistakes, plan


coach_service = CoachService()
