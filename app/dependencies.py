from fastapi import HTTPException

SECURITY_KEY = "pika69"
AUTHORIZED_USERNAME = "PIKACHU_FROM_BD"

def validate_key(username: str, key: str):
    """Validate the security key for restricted usernames."""
    if username == AUTHORIZED_USERNAME:
        if not key or key != SECURITY_KEY:
            raise HTTPException(status_code=403, detail="Unauthorized access.")