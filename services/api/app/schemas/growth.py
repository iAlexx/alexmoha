from pydantic import BaseModel, Field


class ReferralSummaryResponse(BaseModel):
    user_id: str
    referral_code: str
    total_referrals: int
    vip_days_earned: int
    points: int


class ReferralRewardRuleRequest(BaseModel):
    invites_required: int = Field(..., ge=1)
    vip_days_reward: int = Field(..., ge=1)
    points_per_invite: int = Field(default=10, ge=1)


class ReferralRewardRuleResponse(BaseModel):
    invites_required: int
    vip_days_reward: int
    points_per_invite: int
    active: bool


class LeaderboardEntry(BaseModel):
    user_id: str
    points: int


class LeaderboardResponse(BaseModel):
    entries: list[LeaderboardEntry]
    period: str
