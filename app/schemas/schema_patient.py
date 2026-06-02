from pydantic import BaseModel
from typing import Optional
class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    address: str
    disease: str
class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    disease: Optional[str] = None
class PatientResponse(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    phone: str
    address: str
    disease: str
    class Config:
        from_attributes = True