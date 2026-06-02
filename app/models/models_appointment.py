import uuid
from sqlalchemy import Column, String
from app.db.base import Base
class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    patient_name = Column(String)
    disease_id = Column(String)
    disease_name = Column(String)
    doctor_id = Column(String)
    doctor_name = Column(String)
    appointment_date = Column(String)
    appointment_time = Column(String)
    status = Column(
        String,
        default="Booked"
    )