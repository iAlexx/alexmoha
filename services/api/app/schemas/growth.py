from pydantic import BaseModel, Field


class ReferralSummaryResponse(BaseModel):
    user_id: str
    referral_code: str
    total_referrals: int
    vip_days_earned: int


class ReferralRewardRuleRequest(BaseModel):
    invites_required: int = Field(..., ge=1)
    vip_days_reward: int = Field(..., ge=1)


class ReferralRewardRuleResponse(BaseModel):
    invites_required: int
    vip_days_reward: int
    active: bool
