from pydantic import BaseModel


class FailoverFetchResponse(BaseModel):
    source_used: str
    payload_size: int


class SystemHealthResponse(BaseModel):
    database: str
    redis: str
    ai_api: str
    overall: str
