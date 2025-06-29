import uuid
from typing import List
from app.message import MessageModel, MessageStatus

class MessageService:
    def __init__(self):
        self.messages: List[MessageModel] = []

    def create_message(self, text: str, metadata: dict) -> MessageModel:
        message = MessageModel(id=str(uuid.uuid4()), text=text, metadata=metadata)
        self.messages.append(message)
        return message

    def list_messages(self) -> List[MessageModel]:
        return self.messages

    def update_status(self, message_id: str, new_status: MessageStatus) -> MessageModel:
        for msg in self.messages:
            if msg.id == message_id:
                msg.status = new_status
                return msg
        raise ValueError("Message not found")
