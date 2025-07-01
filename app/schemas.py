from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)

class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

class SalaryInfo(BaseModel):
    amount: int
    next_raise_date: datetime
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str
