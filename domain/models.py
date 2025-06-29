from datetime import datetime
from pydantic import BaseModel, Field
from .enums import Status, Visibility, Urgency, Sentiment


class Statement(BaseModel):
    user_id: str
    content: str = Field(max_length=2000)
    status: Status
    visibility: Visibility
    urgency: Urgency = Urgency.medium
    sentiment: Sentiment = Sentiment.neutral
    timestamp: datetime | None = None
    statement_id: str | None = None


class User(BaseModel):
    user_id: str
    cp_balance: int = 999  # 今ラウンドはモック固定
