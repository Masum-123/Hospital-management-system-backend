from app.crud.crud_base import CRUDBase
from app.models.models_doctor import Doctor


class CRUDDoctor(CRUDBase):
    pass


doctor_crud = CRUDDoctor(Doctor)


def create_doctor(db, doctor):
    db_doctor = Doctor(
        name=doctor.name,
        age=doctor.age,
        gender=doctor.gender,
        specialization=doctor.specialization,
        experience=doctor.experience,
        phone=doctor.phone,
        address=doctor.address
    )

    return doctor_crud.create(db, db_doctor)


def get_doctors(db, skip: int = 0, limit: int = 10):
    return doctor_crud.get_all(db, skip, limit)


def update_doctor(db, doctor_id: str, doctor_data):
    return doctor_crud.update(db, doctor_id, doctor_data)


def delete_doctor(db, doctor_id: str):
    return doctor_crud.delete(db, doctor_id)