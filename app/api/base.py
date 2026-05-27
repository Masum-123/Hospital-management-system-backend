from fastapi import APIRouter

from app.api.v1.route_user import router as user_router
from app.api.v1.route_login import router as login_router
from app.api.v1.route_patient import router as patient_router
from app.api.v1.route_doctor import router as doctor_router
from app.api.v1.route_appointment import router as appointment_router
from app.api.v1.route_disease import router as disease_router

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(login_router)
api_router.include_router(patient_router)
api_router.include_router(doctor_router)
api_router.include_router(appointment_router)
api_router.include_router(disease_router)