from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.database import get_db
from app.services.auth_service import authenticate_user, create_access_token
from app.services.user_service import create_user
from app.schemas.user import UserCreate, UserOut
from app.api.deps import get_current_user
from app.services.user_service import UserService
from app.services.auth_service import AuthService

from app.models.user_model import User

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

@router.post("/register", response_model=UserOut)
def register(
    user: UserCreate,
    user_service: UserService = Depends(UserService),
):
    return user_service.register(user)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(AuthService),
):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = auth_service.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def read_users_me(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(AuthService),
):
    user = auth_service.get_current_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
