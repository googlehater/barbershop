from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Score(Base):
    __tablename__ = "scores"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    score_of_master_id: Mapped[int] = mapped_column(
        ForeignKey("masters.id")
    )

    score_by_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    rating: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    feedback_text: Mapped[str | None] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    master = relationship(
        "Master",
        back_populates="scores"
    )

    user = relationship(
        "User",
        back_populates="scores"
    )
