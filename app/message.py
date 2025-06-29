# app/message.py

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Dict
from datetime import datetime, timezone
timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class MessageStatus(str, Enum):
    DRAFT = "draft"
    QUEUED = "queued"
    SENT = "sent"

@dataclass
class MessageModel:
    id: str
    text: str
    status: MessageStatus = MessageStatus.DRAFT
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Optional[Dict] = field(default_factory=dict)
