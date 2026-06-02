from pydantic import BaseModel
from typing import Optional
class DoctorCreate(BaseModel):
    name: str
    age: int
    gender: str
    specialization: str
    experience: int
    phone: str
    address: str
class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    specialization: Optional[str] = None
    experience: Optional[int] = None
    phone: Optional[str] = None
    address: Optional[str] = None
class DoctorResponse(DoctorCreate):
    id: str
    class Config:
        from_attributes = True
class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    specialization: Optional[str] = None
    experience: Optional[int] = None
    phone: Optional[str] = None
    address: Optional[str] = None
class DoctorResponse(DoctorCreate):
    id: str
    class Config:
        from_attributes = True