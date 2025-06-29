import os
from app import config

def test_get_auth_mode(monkeypatch):
    monkeypatch.setenv("AUTH_MODE", "jwt")
    assert config.get_auth_mode() == "jwt"

def test_get_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "abc123")
    assert config.get_api_key() == "abc123"

def test_get_jwt_secret(monkeypatch):
    monkeypatch.setenv("JWT_SECRET", "secret")
    assert config.get_jwt_secret() == "secret"
