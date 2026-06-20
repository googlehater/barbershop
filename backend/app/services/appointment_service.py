from sqlalchemy.orm import Session
from app.models.appointment_model import Appointment
from app.schemas.appointment import AppointmentCreate
from datetime import datetime

class AppointmentService:
    def __init__(self, db: Session):
        self.db = db

    def create_appointment(self, user_id: int, apt_data: AppointmentCreate):
        db_apt = Appointment(
            user_id=user_id,
            master_id=apt_data.master_id,
            service_id=apt_data.service_id,
            appointment_date=apt_data.appointment_date,
            client_wish=apt_data.client_wish,
            created_at=datetime.utcnow(),
            status="confirmed"
        )
        self.db.add(db_apt)
        self.db.commit()
        self.db.refresh(db_apt)
        return db_apt

    def get_user_appointments(self, user_id: int):
        return self.db.query(Appointment).filter(Appointment.user_id == user_id).all()
    