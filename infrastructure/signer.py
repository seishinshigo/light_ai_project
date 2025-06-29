import nacl.signing
import nacl.encoding
import hashlib

_signing_key = nacl.signing.SigningKey.generate()
_verify_key = _signing_key.verify_key


def sign_entry(user_id: str, timestamp: str, content: str) -> tuple[str, str]:
    msg = f"{user_id}{timestamp}{content}"
    hash_hex = hashlib.sha256(msg.encode()).hexdigest()
    signature = _signing_key.sign(hash_hex.encode(), encoder=nacl.encoding.Base64Encoder)
    return hash_hex, signature.signature.decode()


def verify_signature(hash_hex: str, signature_b64: str) -> bool:
    try:
        _verify_key.verify(hash_hex.encode(), nacl.encoding.Base64Encoder.decode(signature_b64))
        return True
    except Exception:
        return False
