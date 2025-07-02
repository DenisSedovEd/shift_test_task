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
def get_salary(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_session)
):
    """
    Маршрутная функция, в случае проверки валидности токена возвращает данные о Salary.
    :param current_user: Пользователь, для которого считывается salary.
    :param db: Автоматически полученная сессия.
    :return: salary
    """
    salary = db.query(Salary).filter(Salary.user_id == current_user.id).first()
    if not salary:
        raise HTTPException(status_code=404, detail="Salary not found")
    return {"salary": salary.amount, "next_raise_date": salary.next_raise_date}
