from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from models import Base

if TYPE_CHECKING:
    from models import Salary


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
    salaries: Mapped[list["Salary"]] = relationship(
        "Salary",
        back_populates="user",
    )
