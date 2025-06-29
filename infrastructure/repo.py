# infrastructure/repo.py
from typing import Dict
from datetime import datetime, UTC
from domain.models import User, Statement
import uuid

# ─────────────────────────────────────────────────────────────
# インメモリの簡易リポジトリ（次ラウンドで DB/Redis に差し替え予定）
# ─────────────────────────────────────────────────────────────
_users: Dict[str, User] = {}
_statements: Dict[str, Statement] = {}


class UserRepo:
    @staticmethod
    async def get(user_id: str) -> User:
        """ユーザー取得（なければ初期CP=999で生成）"""
        if user_id not in _users:
            _users[user_id] = User(user_id=user_id)  # モック: 残高999
        return _users[user_id]

    @staticmethod
    async def update(user: User):
        _users[user.user_id] = user


class StatementRepo:
    @staticmethod
    async def save(stmt: Statement) -> str:
        """draft / queued のステートメントを保存"""
        stmt.statement_id = stmt.statement_id or f"stmt_{uuid.uuid4().hex[:8]}"
        stmt.timestamp = stmt.timestamp or datetime.now(UTC)
        _statements[stmt.statement_id] = stmt
        return stmt.statement_id

    @staticmethod
    async def mark_sent(statement_id: str):
        """送信完了にステータス更新"""
        if statement_id in _statements:
            _statements[statement_id].status = "sent"
