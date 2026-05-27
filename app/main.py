from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

from app.models.models_user import User
from app.models.models_patient import Patient
from app.models.models_doctor import Doctor
from app.models.models_appointment import Appointment
from app.models.models_disease import Disease

from app.api.base import api_router


app = FastAPI(title="Hospital Management System")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/")
def home():
    return {"message": "HMS API Running Successfully"}