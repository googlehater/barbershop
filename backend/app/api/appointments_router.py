from fastapi import APIRouter, Depends, HTTPException
from app.services.appointment_service import AppointmentService
from app.schemas.appointment import AppointmentCreate, AppointmentOut
from app.models.user_model import User
from app.api.deps import get_current_user

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/", response_model=AppointmentOut)
def create_appointment(
    apt: AppointmentCreate,
    current_user: User = Depends(get_current_user),
    appointment_service: AppointmentService = Depends(AppointmentService),
):
    return appointment_service.create_appointment(current_user.id, apt)

@router.get("/my", response_model=list[AppointmentOut])
def get_my_appointments(
    current_user: User = Depends(get_current_user),
    appointment_service: AppointmentService = Depends(AppointmentService),
):
    return appointment_service.get_user_appointments(current_user.id)
