from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models.db import get_session
from models import User, Salary

import config

from jwt import decode
from schemas import SalaryInfo
from security import get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.get("/salary")
def get_salary(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    try:
        payload = decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        # Достаём зарплату только для текущего пользователя
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        salary = db.query(Salary).filter(Salary.user_id == user.id).first()
        return {"salary": salary.amount, "next_raise_date": salary.next_raise_date}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
