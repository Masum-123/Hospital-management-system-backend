from enum import Enum
from pydantic import BaseModel, EmailStr
class UserRole(str, Enum):
    doctor = "doctor"
    patient = "patient"
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: UserRole
    class Config:
        from_attributes = True