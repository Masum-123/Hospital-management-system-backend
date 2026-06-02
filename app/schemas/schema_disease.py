from pydantic import BaseModel
from typing import List, Optional
class DiseaseCreate(BaseModel):
    disease_name: str
    specialized_doctor_id: List[str]
class DiseaseUpdate(BaseModel):
    disease_name: Optional[str] = None
    specialized_doctor_id: Optional[List[str]] = None
class DiseaseResponse(BaseModel):
    id: str
    disease_name: str
    specialized_doctor_id: List[str]
    class Config:
        from_attributes = True