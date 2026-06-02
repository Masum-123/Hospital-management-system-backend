from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.schema_user import UserLogin
from app.crud.crud_user import authenticate_user
from app.core.security import create_access_token
router = APIRouter(
    prefix="/login",
    tags=["Login"]
)
@router.post("/")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "sub": db_user.email,
        "user_id": str(db_user.id),
        "role": db_user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": db_user.role
    }