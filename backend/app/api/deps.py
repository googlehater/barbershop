from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth_service import get_current_user as _get_current_user
from app.services.appointment_service import AppointmentService
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.services.admin_service import AdminService
from app.services.service_service import ServiceService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = _get_current_user(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(db)

def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)

def get_appointment_service(db: Session = Depends(get_db)):
    return AppointmentService(db)

def get_admin_service(db: Session = Depends(get_db)):
    return AdminService(db)

def get_service_service(db: Session = Depends(get_db)):
    return ServiceService(db)
