from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.auth import (
    authenticate_user, create_access_token, get_password_hash, get_current_user
)
from app.core.database import get_session
from app.views.user import UserCreate, UserPublic
from app.models.user import User

auth_router = APIRouter()

# @auth_router.post("/token", response_model=dict)
# async def login_for_access_token(db: Session = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()):
    # user = authenticate_user(db, form_data.username, form_data.password)
    # if not user:
        # raise HTTPException(
            # status_code=status.HTTP_401_UNAUTHORIZED,
            # detail="Incorrect username or password",
            # headers={"WWW-Authenticate": "Bearer"},
        # )
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    # access_token = create_access_token(
        # data={"sub": user.username}, expires_delta=access_token_expires
    # )
    # refresh_token = create_refresh_token(
        # data={"sub": user.username}, expires_delta=refresh_token_expires
    # )
    # return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# @auth_router.post("/refresh-token", response_model=dict)
# async def refresh_access_token(refresh_token: str, db: Session = Depends(get_session)):
    # credentials_exception = HTTPException(
        # status_code=status.HTTP_401_UNAUTHORIZED,
        # detail="Could not validate credentials",
        # headers={"WWW-Authenticate": "Bearer"},
    # )
    # try:
        # payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        # username: str = payload.get("sub")
        # if username is None:
            # raise credentials_exception
    # except JWTError:
        # raise credentials_exception
    # user = get_user(db, username=username)
    # if user is None:
        # raise credentials_exception
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token = create_access_token(
        # data={"sub": user.username}, expires_delta=access_token_expires
    # )
    # return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/register", response_model=UserPublic)
async def register_user(user: UserCreate, db: Session = Depends(get_session)):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserPublic(**db_user.__dict__)