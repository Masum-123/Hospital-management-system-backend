from pydantic import BaseModel


class AppointmentCreate(BaseModel):

    patient_name: str

    disease_id: str

    doctor_id: str

    appointment_date: str

    appointment_time: str


class AppointmentResponse(BaseModel):

    id: str

    patient_name: str

    disease_name: str

    doctor_name: str

    appointment_date: str

    appointment_time: str

    status: str

    class Config:
        from_attributes = True