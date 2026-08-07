from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.repositories.user_repository import UserRepository
from app.api.deps import DBSession
from app.models.user import UserCreate, UserRead
from app.services.auth_services import AuthService
router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/api/v1/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: DBSession):
    service = AuthService(UserRepository(db))

    return service.register(payload)



@router.post("/api/v1/login")
def login (email: str, password: str, db: DBSession):
    service = AuthService(UserRepository(db))
    token = service.login(email, password)

    return {"access_token:": token, "token_type": "bearer"}



@router.post("/api/v1/token")
def get_token (db: DBSession, form:OAuth2PasswordRequestForm = Depends()):
    email = form.username
    password = form.password
    service = AuthService(UserRepository(db))
    token = service.login(email, password)

    return {"access_token": token, "token_type": "bearer"}