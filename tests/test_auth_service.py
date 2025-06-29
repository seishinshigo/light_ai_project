# tests/test_auth_service.py
import pytest
from app.auth_service import AuthService, AuthError

def test_api_key_auth_success():
    auth = AuthService(mode="api_key", credentials={"api_key": "test-1234"})
    result = auth.authenticate()
    assert result.startswith("Authenticated with API Key")

def test_jwt_auth_success():
    auth = AuthService(mode="jwt", credentials={"jwt": "token-abcde"})
    result = auth.authenticate()
    assert result.startswith("Authenticated with JWT")

def test_invalid_mode():
    auth = AuthService(mode="unknown", credentials={})
    with pytest.raises(AuthError):
        auth.authenticate()

def test_missing_api_key():
    auth = AuthService(mode="api_key", credentials={})
    with pytest.raises(AuthError):
        auth.authenticate()

def test_missing_jwt():
    auth = AuthService(mode="jwt", credentials={})
    with pytest.raises(AuthError):
        auth.authenticate()
