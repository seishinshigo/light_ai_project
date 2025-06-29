from dotenv import load_dotenv
import os

# .env 読み込み
load_dotenv()

def get_auth_mode():
    return os.getenv("AUTH_MODE", "api_key")

def get_api_key():
    return os.getenv("API_KEY")

def get_jwt_secret():
    return os.getenv("JWT_SECRET")
