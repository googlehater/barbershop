from sqlalchemy.orm import Session
from app.models.service_model import Service

class ServiceService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_services(self):
        return self.db.query(Service).all()