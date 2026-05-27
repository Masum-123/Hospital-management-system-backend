from sqlalchemy.orm import Session
from app.models.models_doctor import Doctor


def create_doctor(db: Session, doctor):
    db_doctor = Doctor(
        name=doctor.name,
        age=doctor.age,
        gender=doctor.gender,
        specialization=doctor.specialization,
        experience=doctor.experience,
        phone=doctor.phone,
        address=doctor.address
    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def get_doctors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Doctor).offset(skip).limit(limit).all()


def update_doctor(db: Session, doctor_id: str, doctor_data):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        return None

    for key, value in doctor_data.model_dump(exclude_unset=True).items():
        setattr(doctor, key, value)

    db.commit()
    db.refresh(doctor)

    return doctor


def delete_doctor(db: Session, doctor_id: str):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        return None

    db.delete(doctor)
    db.commit()

    return doctor