from fastapi import APIRouter, Query

from app.schemas.growth import ReferralRewardRuleRequest, ReferralRewardRuleResponse, ReferralSummaryResponse
from app.services.growth import GrowthService

router = APIRouter()


@router.get('/referrals/{user_id}', response_model=ReferralSummaryResponse)
def referral_summary(user_id: str, total_referrals: int = Query(0, ge=0)) -> ReferralSummaryResponse:
    return GrowthService.summary(user_id=user_id, total_referrals=total_referrals)


@router.get('/referral-rules', response_model=ReferralRewardRuleResponse)
def referral_rule() -> ReferralRewardRuleResponse:
    return GrowthService.get_rule()


@router.put('/referral-rules', response_model=ReferralRewardRuleResponse)
def update_referral_rule(payload: ReferralRewardRuleRequest) -> ReferralRewardRuleResponse:
    return GrowthService.update_rule(payload.invites_required, payload.vip_days_reward)
