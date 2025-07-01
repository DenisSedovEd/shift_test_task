from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jwt import encode, decode
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import Token

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=30)
    access_token = encode(
        {"sub": user.username, "exp": datetime.utcnow() + access_token_expires},
        "your-secret-key",
        algorithm="HS256"
    )
    return {"access_token": access_token, "token_type": "bearer"}
