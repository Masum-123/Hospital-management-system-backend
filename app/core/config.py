from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
SECRET_KEY = "secret123"
ALGORITHM = "HS256"
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# ✅ THIS IS THE KEY CHANGE (Swagger will show ONLY token box)
bearer_scheme = HTTPBearer()
def hash_password(password: str):
    return pwd_context.hash(password)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ✅ SIMPLE TOKEN AUTH (NO USERNAME/PASSWORD IN SWAGGER)
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user = payload.get("sub")

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return user

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )