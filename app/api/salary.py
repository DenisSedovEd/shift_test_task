from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.db import get_session
from models import User, Salary
from schemas import SalaryInfo
from security import get_current_user

router = APIRouter()


@router.get("/salary", response_model=SalaryInfo)
def get_salary(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_session)
):
    salary = db.query(Salary).filter(Salary.user_id == current_user.id).first()
    if not salary:
        raise HTTPException(status_code=404, detail="Salary information not found")
    return salary
