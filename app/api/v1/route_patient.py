from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.schema_patient import (
    PatientCreate,
    PatientUpdate,
    PatientResponse
)

from app.crud.crud_patient import (
    create_patient,
    get_patients,
    update_patient,
    delete_patient
)

from app.core.security import get_current_user


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post(
    "/",
    response_model=PatientResponse,
    summary="Create Patient"
)
def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return create_patient(db, patient)


@router.get(
    "/",
    response_model=list[PatientResponse],
    summary="Read Patients With Pagination"
)
def read_patients(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return get_patients(db, skip, limit)


@router.patch(
    "/{patient_id}",
    response_model=PatientResponse,
    summary="Update Patient"
)
def patch_patient(
    patient_id: str,
    patient: PatientUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    updated = update_patient(db, patient_id, patient)

    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")

    return updated


@router.delete(
    "/{patient_id}",
    summary="Delete Patient"
)
def remove_patient(
    patient_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    deleted = delete_patient(db, patient_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Patient not found")

    return {"message": "Patient deleted successfully"}