from datetime import date

from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Numeric
from sqlalchemy import Enum

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import Base

import enum


class MasterStatus(str, enum.Enum):
    fired = "fired"
    works = "works"
    on_vacation = "on_vacation"


class Master(Base):
    __tablename__ = "masters"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(20)
    )

    average_score: Mapped[float | None] = mapped_column(
        Numeric(3, 2)
    )

    works_since: Mapped[date | None] = mapped_column(
        Date
    )

    status: Mapped[MasterStatus] = mapped_column(
        Enum(MasterStatus),
        default=MasterStatus.works
    )

    appointments = relationship(
        "Appointment",
        back_populates="master"
    )

    scores = relationship(
        "Score",
        back_populates="master"
    )
