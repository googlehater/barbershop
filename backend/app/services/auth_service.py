import bcrypt
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.auth import TokenData
import os
from app.models.user_model import User
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

class AuthService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_password_hash(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    def authenticate_user(self, username: str, password: str):
        user = self.db.query(User).filter(User.username == username).first()
        if not user or not self.verify_password(password, user.password_hash):
            return None
        return user
    
    def get_current_user(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                return None
            return self.db.query(User).filter(User.username == username).first()
        except JWTError:
            return None
        