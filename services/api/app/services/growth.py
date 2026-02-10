import hashlib

from app.schemas.growth import (
    LeaderboardEntry,
    LeaderboardResponse,
    ReferralRewardRuleResponse,
    ReferralSummaryResponse,
)


class GrowthService:
    _rule = ReferralRewardRuleResponse(invites_required=5, vip_days_reward=7, points_per_invite=10, active=True)

    @staticmethod
    def build_referral_code(user_id: str) -> str:
        return hashlib.md5(user_id.encode('utf-8')).hexdigest()[:8].upper()

    @classmethod
    def summary(cls, user_id: str, total_referrals: int) -> ReferralSummaryResponse:
        cycles = total_referrals // cls._rule.invites_required
        vip_days = cycles * cls._rule.vip_days_reward
        points = total_referrals * cls._rule.points_per_invite
        return ReferralSummaryResponse(
            user_id=user_id,
            referral_code=cls.build_referral_code(user_id),
            total_referrals=total_referrals,
            vip_days_earned=vip_days,
            points=points,
        )

    @classmethod
    def get_rule(cls) -> ReferralRewardRuleResponse:
        return cls._rule

    @classmethod
    def update_rule(cls, invites_required: int, vip_days_reward: int, points_per_invite: int) -> ReferralRewardRuleResponse:
        cls._rule = ReferralRewardRuleResponse(
            invites_required=invites_required,
            vip_days_reward=vip_days_reward,
            points_per_invite=points_per_invite,
            active=True,
        )
        return cls._rule

    @classmethod
    def leaderboard(cls, period: str = 'weekly') -> LeaderboardResponse:
        # Placeholder static ranking until DB integration.
        entries = [
            LeaderboardEntry(user_id='user_top_1', points=1320),
            LeaderboardEntry(user_id='user_top_2', points=1180),
            LeaderboardEntry(user_id='user_top_3', points=950),
        ]
        return LeaderboardResponse(entries=entries, period=period)
