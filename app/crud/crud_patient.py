from app.crud.crud_base import CRUDBase
from app.models.models_patient import Patient


class CRUDPatient(CRUDBase):
    pass


patient_crud = CRUDPatient(Patient)


def create_patient(db, patient):
    db_patient = Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address,
        disease=patient.disease
    )

    return patient_crud.create(db, db_patient)


def get_patients(db, skip: int = 0, limit: int = 10):
    return patient_crud.get_all(db, skip, limit)


def update_patient(db, patient_id: str, patient_data):
    return patient_crud.update(db, patient_id, patient_data)


def delete_patient(db, patient_id: str):
    return patient_crud.delete(db, patient_id)