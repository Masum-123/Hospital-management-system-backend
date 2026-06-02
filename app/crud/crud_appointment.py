from app.crud.crud_base import CRUDBase

from app.models.models_appointment import Appointment
from app.models.models_disease import Disease
from app.models.models_doctor import Doctor


ALL_SLOTS = [
    "09:00 AM",
    "10:00 AM",
    "11:00 AM",
    "12:00 PM",
    "02:00 PM",
    "03:00 PM",
    "04:00 PM",
    "05:00 PM"
]


class CRUDAppointment(CRUDBase):
    pass


appointment_crud = CRUDAppointment(Appointment)


def get_available_slots(db, doctor_id: str, appointment_date: str):
    booked = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id,
        Appointment.appointment_date == appointment_date
    ).all()

    booked_slots = [
        b.appointment_time
        for b in booked
    ]

    return [
        {
            "slot": slot,
            "status": "Booked" if slot in booked_slots else "Available"
        }
        for slot in ALL_SLOTS
    ]


def create_appointment(db, appointment):
    disease = db.query(Disease).filter(
        Disease.id == appointment.disease_id
    ).first()

    if not disease:
        return "Disease not found"

    doctor = db.query(Doctor).filter(
        Doctor.id == appointment.doctor_id
    ).first()

    if not doctor:
        return "Doctor not found"

    slots = get_available_slots(
        db,
        appointment.doctor_id,
        appointment.appointment_date
    )

    selected_slot = None

    for slot in slots:
        if slot["slot"] == appointment.appointment_time:
            selected_slot = slot

    if not selected_slot:
        return "Invalid slot"

    if selected_slot["status"] == "Booked":
        return "Slot already booked"

    db_appointment = Appointment(
        patient_name=appointment.patient_name,
        disease_id=disease.id,
        disease_name=disease.disease_name,
        doctor_id=doctor.id,
        doctor_name=doctor.name,
        appointment_date=appointment.appointment_date,
        appointment_time=appointment.appointment_time,
        status="Booked"
    )

    return appointment_crud.create(db, db_appointment)


def get_appointments(db):
    return appointment_crud.get_all(db)