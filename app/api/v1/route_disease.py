from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.schema_disease import DiseaseCreate, DiseaseUpdate, DiseaseResponse
from app.crud.crud_disease import (
    create_disease,
    get_diseases,
    update_disease,
    delete_disease
)
router = APIRouter(
    prefix="/diseases",
    tags=["Disease Management"]
)
@router.post("/", response_model=DiseaseResponse)
def add_disease(disease: DiseaseCreate, db: Session = Depends(get_db)):
    return create_disease(db, disease)


@router.get("/", response_model=list[DiseaseResponse])
def read_diseases(db: Session = Depends(get_db)):
    return get_diseases(db)


@router.patch("/{disease_id}", response_model=DiseaseResponse)
def patch_disease(disease_id: str, disease: DiseaseUpdate, db: Session = Depends(get_db)):
    updated = update_disease(db, disease_id, disease)

    if not updated:
        raise HTTPException(status_code=404, detail="Disease not found")

    return updated


@router.delete("/{disease_id}")
def remove_disease(disease_id: str, db: Session = Depends(get_db)):
    deleted = delete_disease(db, disease_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Disease not found")

    return {"message": "Disease deleted successfully"}