from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "burger_secret_key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )