from sqlalchemy.orm import Session
from app.models.models_patient import Patient


def create_patient(db: Session, patient):
    db_patient = Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address,
        disease=patient.disease
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient


def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Patient).offset(skip).limit(limit).all()


def update_patient(db: Session, patient_id: str, patient_data):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        return None

    for key, value in patient_data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)

    return patient


def delete_patient(db: Session, patient_id: str):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        return None

    db.delete(patient)
    db.commit()

    return patient