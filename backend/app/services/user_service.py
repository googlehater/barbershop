from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user_model import User
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.auth_service = AuthService(db)
    
    def register(self, user_data: UserCreate):
        existing = self.db.query(User).filter(User.username == user_data.username).first()
        if existing:
            raise HTTPException(status_code=400, detail="Username already registered")
        
        hashed_password = self.auth_service.get_password_hash(user_data.password)
        db_user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=hashed_password,
            role=user_data.role,
            created_at=datetime.utcnow()
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    