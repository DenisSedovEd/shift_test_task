from pydantic import BaseModel, Field
from datetime import datetime

from sqlalchemy import DateTime


class UserCreate(BaseModel):
    """
    Схема для создания User.
    """

    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)


class UserResponse(BaseModel):
    """
    Схема для запроса User.
    """

    id: int
    username: str
    created_at: datetime


class SalaryInfo(BaseModel):
    """
    Схема для запроса Salary.
    """

    amount: int
    next_raise_date: datetime
    created_at: datetime


class Token(BaseModel):
    """
    Схема Token.
    """

    access_token: str
    token_type: str
