from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from app.core.db import get_session
from app.core.security import decode_token
from app.models.user import User
from app.repositories.user_repository import UserRepository

# obtencion de token bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/api/v1/token", auto_error=False)
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token", auto_error=False)

def get_db() -> Session:
    #se obtiene el 1er valor de get_session
    return next(get_session())



# Antes -> db:  Session = Depends(get_db)
# Ahora -> db: DBSession
DBSession = Annotated[Session, Depends(get_db)]



def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: DBSession) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autorizado, no sub",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        # user_id = int(payload.get("sub"))
    except Exception:
        raise credentials_exception

    repository = UserRepository(db)
    user = repository.get_by_id(user_id)
    if not user:
        raise credentials_exception

    return user



CurrentUser = Annotated[User, Depends(get_current_user)]