from app.crud.crud_base import CRUDBase
from app.models.models_user import User

from app.core.security import (
    hash_password,
    verify_password
)


class CRUDUser(CRUDBase):
    pass


user_crud = CRUDUser(User)


def create_user(db, user):
    db_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    return user_crud.create(db, db_user)


def get_users(db, skip: int = 0, limit: int = 10):
    return user_crud.get_all(db, skip, limit)


def get_user_by_id(db, user_id: str):
    return user_crud.get_by_id(db, user_id)


def update_user(db, user_id: str, user_data):
    return user_crud.update(db, user_id, user_data)


def delete_user(db, user_id: str):
    return user_crud.delete(db, user_id)


def authenticate_user(db, email: str, password: str):
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user