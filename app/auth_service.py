# app/auth_service.py
class AuthError(Exception):
    pass

class AuthService:
    def __init__(self, mode: str, credentials: dict):
        # mode: "api_key" または "jwt"
        self.mode = mode
        self.credentials = credentials

    def authenticate(self):
        if self.mode == "api_key":
            return self._authenticate_api_key()
        elif self.mode == "jwt":
            return self._authenticate_jwt()
        else:
            raise AuthError(f"Unknown auth mode: {self.mode}")

    def _authenticate_api_key(self):
        api_key = self.credentials.get("api_key")
        if not api_key:
            raise AuthError("Missing API Key")
        # 実際のAPI Key検証は外部サービスに委ねるが、ここでは簡易チェック
        return f"Authenticated with API Key: {api_key[:4]}***"

    def _authenticate_jwt(self):
        jwt_token = self.credentials.get("jwt")
        if not jwt_token:
            raise AuthError("Missing JWT token")
        # JWT の検証処理は後のステップで導入。ここではトークン存在のみ確認。
        return f"Authenticated with JWT: {jwt_token[:6]}***"
