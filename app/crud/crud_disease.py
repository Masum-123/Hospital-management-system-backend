from app.crud.crud_base import CRUDBase
from app.models.models_disease import Disease


class CRUDDisease(CRUDBase):
    pass


disease_crud = CRUDDisease(Disease)


def create_disease(db, disease):
    db_disease = Disease(
        disease_name=disease.disease_name,
        specialized_doctor_id=disease.specialized_doctor_id
    )

    return disease_crud.create(db, db_disease)


def get_diseases(db, skip: int = 0, limit: int = 10):
    return disease_crud.get_all(db, skip, limit)


def update_disease(db, disease_id: str, disease_data):
    return disease_crud.update(db, disease_id, disease_data)


def delete_disease(db, disease_id: str):
    return disease_crud.delete(db, disease_id)