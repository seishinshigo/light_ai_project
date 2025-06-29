import pytest
from app.message import MessageModel, MessageStatus
from app.message_service import MessageService
from app.cp_service import CPService, CPInsufficientError

def test_create_message():
    cp_service = CPService(initial_balance=100)
    service = MessageService(cp_service=cp_service)
    message = service.create_message("Hello", {"source": "test"})
    assert message.text == "Hello"
    assert message.status == MessageStatus.DRAFT
    assert message.metadata == {"source": "test"}

def test_list_messages():
    cp_service = CPService(initial_balance=100)
    service = MessageService(cp_service=cp_service)
    service.create_message("One", {})
    service.create_message("Two", {})
    messages = service.list_messages()
    assert len(messages) == 2

def test_update_status():
    cp_service = CPService(initial_balance=100)
    service = MessageService(cp_service=cp_service)
    message = service.create_message("Change me", {})
    updated = service.update_status(message.id, MessageStatus.QUEUED)
    assert updated.status == MessageStatus.QUEUED

def test_reserve_message_success():
    """メッセージの予約が成功するケース"""
    cp_service = CPService(initial_balance=100)
    service = MessageService(cp_service=cp_service)
    message = service.create_message("Reserve me", {"original": "data"})
    
    reserved_message = service.reserve_message(
        message=message, 
        cp_cost=30, 
        metadata={"reserved_at": "2025-06-29"}
    )
    
    assert reserved_message.status == MessageStatus.QUEUED
    assert cp_service.balance == 70
    assert reserved_message.metadata == {"original": "data", "reserved_at": "2025-06-29"}

def test_reserve_message_insufficient_cp():
    """CP不足でメッセージの予約が失敗するケース"""
    cp_service = CPService(initial_balance=20)
    service = MessageService(cp_service=cp_service)
    message = service.create_message("Can't reserve", {})
    
    with pytest.raises(CPInsufficientError):
        service.reserve_message(message=message, cp_cost=50, metadata={})
        
    assert message.status == MessageStatus.DRAFT # Status should not change
    assert cp_service.balance == 20 # Balance should not change

def test_reserve_message_metadata_update():
    """メタデータが正しく更新されることを確認する"""
    cp_service = CPService(initial_balance=100)
    service = MessageService(cp_service=cp_service)
    # Start with empty metadata
    message = service.create_message("Metadata test", {})
    
    service.reserve_message(
        message=message, 
        cp_cost=10, 
        metadata={"user_id": 123, "priority": "high"}
    )
    
    assert message.metadata == {"user_id": 123, "priority": "high"}
    
    # Test with pre-existing metadata
    message2 = service.create_message("Metadata test 2", {"source": "web"})
    service.reserve_message(
        message=message2,
        cp_cost=10,
        metadata={"status": "pending"}
    )
    assert message2.metadata == {"source": "web", "status": "pending"}
