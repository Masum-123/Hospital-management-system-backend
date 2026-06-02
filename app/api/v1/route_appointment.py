from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.models_disease import Disease
from app.models.models_doctor import Doctor

from app.schemas.schema_appointment import (
    AppointmentCreate,
    AppointmentResponse
)

from app.crud.crud_appointment import (
    create_appointment,
    get_appointments,
    get_available_slots
)


router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.get("/diseases")
def get_diseases(
    db: Session = Depends(get_db)
):
    diseases = db.query(Disease).all()

    return [
        {
            "disease_id": d.id,
            "disease_name": d.disease_name
        }
        for d in diseases
    ]


@router.get("/doctors/{disease_id}")
def disease_doctors(
    disease_id: str,
    db: Session = Depends(get_db)
):
    disease = db.query(Disease).filter(
        Disease.id == disease_id
    ).first()

    if not disease:
        raise HTTPException(
            status_code=404,
            detail="Disease not found"
        )

    doctors = db.query(Doctor).filter(
        Doctor.id.in_(
            disease.specialized_doctor_id
        )
    ).all()

    return {
        "doctors": [
            {
                "doctor_id": doctor.id,
                "doctor_name": doctor.name
            }
            for doctor in doctors
        ]
    }


@router.get("/slots/{doctor_id}/{appointment_date}")
def doctor_slots(
    doctor_id: str,
    appointment_date: str,
    db: Session = Depends(get_db)
):
    return get_available_slots(
        db,
        doctor_id,
        appointment_date
    )


@router.post(
    "/",
    response_model=AppointmentResponse
)
def book_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):
    result = create_appointment(
        db,
        appointment
    )

    if isinstance(result, str):
        raise HTTPException(
            status_code=400,
            detail=result
        )

    return result


@router.get(
    "/",
    response_model=list[AppointmentResponse]
)
def all_appointments(
    db: Session = Depends(get_db)
):
    return get_appointments(db)