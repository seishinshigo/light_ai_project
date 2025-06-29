from app.message import MessageModel, MessageStatus
from app.message_service import MessageService

def test_create_message():
    service = MessageService()
    message = service.create_message("Hello", {"cp": 10})
    assert message.text == "Hello"
    assert message.status == MessageStatus.DRAFT

def test_list_messages():
    service = MessageService()
    service.create_message("One", {"cp": 10})
    service.create_message("Two", {"cp": 20})
    messages = service.list_messages()
    assert len(messages) == 2

def test_update_status():
    service = MessageService()
    message = service.create_message("Change me", {"cp": 0})
    updated = service.update_status(message.id, MessageStatus.QUEUED)
    assert updated.status == MessageStatus.QUEUED
