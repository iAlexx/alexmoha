from fastapi import APIRouter

from app.schemas.social import SentimentVoteRequest, SentimentVoteResponse, WhaleWatchRequest, WhaleWatchResponse
from app.services.social import social_service

router = APIRouter()


@router.post('/sentiment-vote', response_model=SentimentVoteResponse)
def sentiment_vote(payload: SentimentVoteRequest) -> SentimentVoteResponse:
    return social_service.vote(payload.news_id, payload.vote)


@router.post('/whale-watch', response_model=WhaleWatchResponse)
def whale_watch(payload: WhaleWatchRequest) -> WhaleWatchResponse:
    return social_service.whale_watch(payload.asset, payload.transfer_usd, payload.related_news_id)
