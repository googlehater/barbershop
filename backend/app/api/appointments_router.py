from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user_model import User
from app.models.appointment_model import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentOut
from app.api.deps import get_current_user

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/", response_model=AppointmentOut)
def create_appointment(
    apt: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_apt = Appointment(
        user_id=current_user.id,
        master_id=apt.master_id,
        service_id=apt.service_id,
        appointment_date=apt.appointment_date,
        client_wish=apt.client_wish,
        status="confirmed"
    )
    db.add(db_apt)
    db.commit()
    db.refresh(db_apt)
    return db_apt

@router.get("/my", response_model=list[AppointmentOut])
def get_my_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appointments = db.query(Appointment).filter(Appointment.user_id == current_user.id).all()
    return appointments
