from sqlalchemy.orm import Session
from app.models.models_user import User
from app.schemas.schema_user import UserCreate
from app.core.security import (
    hash_password,
    verify_password
)

def create_user(db: Session, user: UserCreate):

    hashed = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    return user