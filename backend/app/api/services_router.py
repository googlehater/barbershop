from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.service_model import Service

router = APIRouter(prefix="/services", tags=["services"])

@router.get("/")
def get_services(db: Session = Depends(get_db)):
    return db.query(Service).all()
