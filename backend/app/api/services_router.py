from fastapi import APIRouter, Depends
from app.services.service_service import ServiceService
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/services", tags=["services"])

def get_service_service(db: Session = Depends(get_db)):
    return ServiceService(db)

@router.get("/")
def get_services(
    service_service: ServiceService = Depends(get_service_service),
):
    return service_service.get_all_services()
