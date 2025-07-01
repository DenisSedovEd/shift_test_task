from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jwt import encode, decode
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from random import randint

from models.db import get_session
from models import User, Salary
from schemas import Token, UserCreate, UserResponse
import config

router = APIRouter()

pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_session)):
    # Проверяем, не существует ли уже пользователь с таким именем
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    # Хэшируем пароль
    hashed_password = pwd_context.hash(user.password)

    # Создаем нового пользователя
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserResponse(
        id=db_user.id, username=db_user.username, created_at=db_user.created_at
    )


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)
):
    print("SECRET_KEY:", config.SECRET_KEY)
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    exp = datetime.utcnow() + access_token_expires
    access_token = encode(
        {"sub": user.username, "exp": int(exp.timestamp())},
        config.SECRET_KEY,
        config.ALGORITHM,
    )
    return {"access_token": access_token, "token_type": "bearer"}
