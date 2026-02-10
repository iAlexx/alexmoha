import hashlib

from app.schemas.growth import ReferralRewardRuleResponse, ReferralSummaryResponse


class GrowthService:
    _rule = ReferralRewardRuleResponse(invites_required=5, vip_days_reward=7, active=True)

    @staticmethod
    def build_referral_code(user_id: str) -> str:
        return hashlib.md5(user_id.encode('utf-8')).hexdigest()[:8].upper()

    @classmethod
    def summary(cls, user_id: str, total_referrals: int) -> ReferralSummaryResponse:
        cycles = total_referrals // cls._rule.invites_required
        vip_days = cycles * cls._rule.vip_days_reward
        return ReferralSummaryResponse(
            user_id=user_id,
            referral_code=cls.build_referral_code(user_id),
            total_referrals=total_referrals,
            vip_days_earned=vip_days,
        )

    @classmethod
    def get_rule(cls) -> ReferralRewardRuleResponse:
        return cls._rule

    @classmethod
    def update_rule(cls, invites_required: int, vip_days_reward: int) -> ReferralRewardRuleResponse:
        cls._rule = ReferralRewardRuleResponse(
            invites_required=invites_required,
            vip_days_reward=vip_days_reward,
            active=True,
        )
        return cls._rule
