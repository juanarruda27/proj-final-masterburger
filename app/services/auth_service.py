from datetime import datetime, timedelta
from jose import jwt
import hashlib

SECRET_KEY = "burgersystem-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password: str):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()

def verify_password(
    plain_password,
    hashed_password
):

    return (
        hashlib.sha256(
            plain_password.encode()
        ).hexdigest()
        == hashed_password
    )

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )