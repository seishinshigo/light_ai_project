# application/services/statement_service.py

from domain.repositories import UserRepo, StatementRepo, CPRepo
from infrastructure.queue import ObserverQueue

class StatementService:
    MAX_CHAR = 2000
    CP_COST = 200

    def __init__(self, queue: ObserverQueue):
        self.queue = queue

    async def submit_statement(self, stmt):
        if len(stmt.content) > self.MAX_CHAR:
            raise ValueError("文字数制限（2000字）を超えています")

        user = await UserRepo.get(stmt.user_id)
        if user.cp_balance < self.CP_COST:
            raise ValueError("CP残高が不足しています（200CP必要）")

        # ステータスがqueuedのときのみCPを消費
        if stmt.status == "queued":
            await CPRepo.consume(user.id, self.CP_COST, "free_statement")

        # 発言を保存（draftまたはqueued）
        statement_id = await StatementRepo.save(stmt)

        # queuedならば観測者AIに通知キューへ送信
        if stmt.status == "queued":
            payload = {
                "statement_id": statement_id,
                "user_id": stmt.user_id,
                "content": stmt.content,
                "visibility": stmt.visibility,
                "urgency": stmt.urgency,
                "sentiment": stmt.sentiment
            }
            await self.queue.publish(payload)
            await StatementRepo.mark_sent(statement_id)

        return {"status": "ok", "statement_id": statement_id}
