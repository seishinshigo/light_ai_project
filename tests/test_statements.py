import pytest
from httpx import AsyncClient
from app.main import app
from jose import jwt
from app.deps import SECRET, ALGORITHM
from domain.enums import Status, Visibility, Urgency

TOKEN = jwt.encode({"sub": "user001"}, SECRET, algorithm=ALGORITHM)


@pytest.mark.asyncio
async def test_post_statement():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "user_id": "user001",
            "content": "Hello observer AI",
            "status": Status.queued,
            "visibility": Visibility.public,
            "urgency": Urgency.high,
        }
        res = await ac.post("/statements", json=payload, headers={"Authorization": f"Bearer {TOKEN}"})
        assert res.status_code == 200
        assert res.json()["status"] == "ok"
