import pytest
from app.message import MessageModel, MessageStatus
import uuid

def test_message_default_status():
    msg = MessageModel(id=str(uuid.uuid4()), text="Test")
    assert msg.status == MessageStatus.DRAFT
    assert isinstance(msg.id, str)
    assert msg.metadata == {}


def test_message_status_change():
    msg = MessageModel(id=str(uuid.uuid4()), text="Ready")
    msg.status = MessageStatus.QUEUED
    assert msg.status == MessageStatus.QUEUED


def test_message_has_timestamp():
    msg = MessageModel(id=str(uuid.uuid4()), text="Check timestamp")
    assert msg.timestamp is not None
