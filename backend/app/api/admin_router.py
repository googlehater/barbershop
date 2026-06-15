from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user_model import User
from app.models.appointment_model import Appointment
from app.api.deps import get_current_user

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/stats")
def admin_stats(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    total_users = db.query(User).count()
    total_appointments = db.query(Appointment).count()
    return {"total_users": total_users, "total_appointments": total_appointments}
