from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.schema_doctor import (
    DoctorCreate,
    DoctorUpdate,
    DoctorResponse
)
from app.crud.crud_doctor import (
    create_doctor,
    get_doctors,
    update_doctor,
    delete_doctor
)
from app.core.security import get_current_user
router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)
@router.post("/", response_model=DoctorResponse, summary="Add Doctor")
def add_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return create_doctor(db, doctor)
@router.get("/", response_model=list[DoctorResponse], summary="Read Doctors With Pagination")
def read_doctors(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return get_doctors(db, skip, limit)
@router.patch("/{doctor_id}", response_model=DoctorResponse, summary="Update Doctor")
def patch_doctor(
    doctor_id: str,
    doctor: DoctorUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    updated = update_doctor(db, doctor_id, doctor)

    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return updated
@router.delete("/{doctor_id}", summary="Delete Doctor")
def remove_doctor(
    doctor_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    deleted = delete_doctor(db, doctor_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return {"message": "Doctor deleted successfully"}