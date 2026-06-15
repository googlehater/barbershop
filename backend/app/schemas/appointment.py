from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    master_id: int
    service_id: int
    appointment_date: datetime
    client_wish: str | None = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentOut(AppointmentBase):
    id: int
    user_id: int
    created_at: datetime
    status: str

    class Config:
        from_attributes = True
        