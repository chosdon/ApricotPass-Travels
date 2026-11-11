from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Package(Base):
    __tablename__ = "packages"

    __table_args__ = (
        CheckConstraint(
            "duration_days > 0",
            name="positive_duration_days",
        ),
        CheckConstraint(
            "duration_nights >= 0",
            name="nonnegative_duration_nights",
        ),
        CheckConstraint(
            "publication_status IN ('draft', 'published', 'archived')",
            name="valid_publication_status",
        ),
    )

    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    slug: Mapped[str] = mapped_column(String(180), unique=True)
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text)

    duration_days: Mapped[int] = mapped_column(Integer)
    duration_nights: Mapped[int] = mapped_column(Integer)

    publication_status: Mapped[str] = mapped_column(
        String(20),
        server_default="draft",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )