from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.schema_user import UserCreate, UserResponse
from app.crud.crud_user import create_user


router = APIRouter(
    prefix="/register",
    tags=["Register"]
)


@router.post(
    "/",
    response_model=UserResponse
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)