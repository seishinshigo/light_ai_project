import pytest
from app.message import Message, MessageStatus


def test_message_default_status():
    msg = Message(content="Test")
    assert msg.status == MessageStatus.DRAFT
    assert isinstance(msg.id, str)
    assert msg.metadata == {}


def test_message_status_change():
    msg = Message(content="Ready")
    msg.status = MessageStatus.QUEUED
    assert msg.status == MessageStatus.QUEUED


def test_message_has_timestamp():
    msg = Message(content="Check timestamp")
    assert msg.timestamp is not None
