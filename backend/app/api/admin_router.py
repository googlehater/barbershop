from fastapi import APIRouter, Depends, HTTPException
from app.services.admin_service import AdminService
from app.models.user_model import User
from app.api.deps import get_current_user, get_admin_service, get_service_service

from app.core.database import get_db

router = APIRouter(prefix="/admin", tags=["admin"])

def get_admin_service(db: Session = Depends(get_db)):
    return AdminService(db)

@router.get("/stats")
def admin_stats(
    current_user: User = Depends(get_current_user),
    admin_service: AdminService = Depends(get_admin_service),
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return admin_service.get_stats()
