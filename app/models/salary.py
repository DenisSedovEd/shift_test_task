from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models import Base

if TYPE_CHECKING:
    from models import User


class Salary(Base):
    __tablename__ = "salaries"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="salaries",
    )
    amount: Mapped[int] = mapped_column(
        Integer,
    )
    next_raise_data: Mapped[datetime] = mapped_column(
        DateTime,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
