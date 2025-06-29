from enum import Enum


class Status(str, Enum):
    draft = "draft"
    queued = "queued"
    sent = "sent"


class Visibility(str, Enum):
    public = "public"
    limited = "limited"
    private = "private"


class Urgency(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Sentiment(str, Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"
