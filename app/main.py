from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import Optional
from domain.schema import StatementRequest, StatementResponse
from application.statement_service import StatementService
from infrastructure.auth import verify_token

app = FastAPI()
service = StatementService()


@app.get("/")
def read_root():
    return {"message": "Welcome to Light AI API"}


@app.post("/statements", response_model=StatementResponse)
async def submit_statement(
    payload: StatementRequest,
    authorization: str = Header(..., alias="Authorization")
):
    # トークン検証
    if not verify_token(authorization):
        raise HTTPException(status_code=401, detail="Invalid token")

    # 発言処理実行
    result = await service.submit_statement(payload)
    return result


@app.get("/health")
def health_check():
    return {"status": "ok"}
