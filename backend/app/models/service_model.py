from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Numeric

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    services_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    duration_minutes: Mapped[int] = mapped_column(
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    appointments = relationship(
        "Appointment",
        back_populates="service"
    )