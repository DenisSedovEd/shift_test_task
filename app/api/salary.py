from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Salary
from app.schemas import SalaryInfo
from app.security import get_current_user

router = APIRouter()

@router.get("/salary", response_model=SalaryInfo)
def get_salary(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    salary = db.query(Salary).filter(Salary.user_id == current_user.id).first()
    if not salary:
        raise HTTPException(status_code=404, detail="Salary information not found")
    return salary
