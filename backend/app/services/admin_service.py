from sqlalchemy.orm import Session
from app.models.user_model import User
from app.models.appointment_model import Appointment

class AdminService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_stats(self):
        total_users = self.db.query(User).count()
        total_appointments = self.db.query(Appointment).count()
        return {
            "total_users": total_users,
            "total_appointments": total_appointments
        }
    