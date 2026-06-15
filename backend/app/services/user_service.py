from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user import UserCreate
from app.services.auth_service import get_password_hash
from datetime import datetime

def create_user(db: Session, user_create: UserCreate):
    hashed_pw = get_password_hash(user_create.password)
    db_user = User(
        username=user_create.username,
        email=user_create.email,
        password_hash=hashed_pw,
        role=user_create.role,
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
