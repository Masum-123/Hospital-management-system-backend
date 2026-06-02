from pydantic import BaseModel
from enum import Enum


class AppointmentSlot(str, Enum):
    SLOT_1 = "09:00 AM"
    SLOT_2 = "10:00 AM"
    SLOT_3 = "11:00 AM"
    SLOT_4 = "12:00 PM"
    SLOT_5 = "02:00 PM"
    SLOT_6 = "03:00 PM"
    SLOT_7 = "04:00 PM"
    SLOT_8 = "05:00 PM"


class AppointmentCreate(BaseModel):
    patient_name: str
    disease_id: str
    doctor_id: str
    appointment_date: str
    appointment_time: AppointmentSlot


class AppointmentResponse(BaseModel):
    id: str
    patient_name: str
    disease_id: str
    disease_name: str
    doctor_id: str
    doctor_name: str
    appointment_date: str
    appointment_time: str
    status: str

    class Config:
        from_attributes = True