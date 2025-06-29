import uuid
from typing import List, Dict
from app.message import MessageModel, MessageStatus
from app.cp_service import CPService, CPInsufficientError

class MessageService:
    def __init__(self, cp_service: CPService):
        self.messages: List[MessageModel] = []
        self.cp_service = cp_service
        self.cp_service = cp_service

    def create_message(self, text: str, metadata: dict) -> MessageModel:
        message = MessageModel(id=str(uuid.uuid4()), text=text, metadata=metadata)
        self.messages.append(message)
        return message

    def reserve_message(self, message: MessageModel, cp_cost: int, metadata: Dict) -> MessageModel:
        """CPを消費してメッセージを予約する"""
        self.cp_service.consume(cp_cost)
        message.status = MessageStatus.QUEUED
        if message.metadata:
            message.metadata.update(metadata)
        else:
            message.metadata = metadata
        return message

    def list_messages(self) -> List[MessageModel]:
        return self.messages

    def update_status(self, message_id: str, new_status: MessageStatus) -> MessageModel:
        for msg in self.messages:
            if msg.id == message_id:
                msg.status = new_status
                return msg
        raise ValueError("Message not found")
