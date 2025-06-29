from domain.models import Statement
from domain.enums import Status
from infrastructure.repo import UserRepo, StatementRepo
from infrastructure.queue import ObserverQueue
from infrastructure.signer import sign_entry
from pathlib import Path
import json
from datetime import datetime, UTC

LOG_DIR = Path("output_logs/statements")
LOG_DIR.mkdir(parents=True, exist_ok=True)


class StatementService:
    MAX_CHAR = 2000
    CP_COST = 200

    def __init__(self, queue: ObserverQueue):
        self.queue = queue

    async def submit_statement(self, stmt: Statement):
        if len(stmt.content) > self.MAX_CHAR:
            raise ValueError("文字数制限（2000字）を超えています")

        user = await UserRepo.get(stmt.user_id)
        if stmt.status is Status.queued and user.cp_balance < self.CP_COST:
            raise ValueError("CP残高が不足しています（200CP必要）")

        if stmt.status is Status.queued:
            user.cp_balance -= self.CP_COST
            await UserRepo.update(user)

        statement_id = await StatementRepo.save(stmt)

        # 署名ログ
        hash_hex, signature = sign_entry(stmt.user_id, stmt.timestamp.isoformat(), stmt.content)
        self._write_log(stmt, hash_hex, signature)

        if stmt.status is Status.queued:
            await self.queue.publish(stmt.model_dump())
            await StatementRepo.mark_sent(statement_id)

        return {"status": "ok", "statement_id": statement_id}

    def _write_log(self, stmt: Statement, hash_hex: str, signature: str):
        log_path = LOG_DIR / f"statements_log_{datetime.now(UTC):%Y-%m}.jsonl"
        with log_path.open("a", encoding="utf-8") as f:
            entry = stmt.model_dump()
            entry.update(hash=hash_hex, signature=signature)
            # すべての非JSON型は default=str で文字列化
            f.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")
