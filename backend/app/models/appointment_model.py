from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    master_id: Mapped[int] = mapped_column(
        ForeignKey("masters.id")
    )

    service_id: Mapped[int] = mapped_column(
        ForeignKey("services.id")
    )

    client_wish: Mapped[str | None] = mapped_column(
        Text
    )

    appointment_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="confirmed"
    )

    user = relationship(
        "User",
        back_populates="appointments"
    )

    master = relationship(
        "Master",
        back_populates="appointments"
    )

    service = relationship(
        "Service",
        back_populates="appointments"
    )
