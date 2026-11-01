from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description_text: Mapped[str] = mapped_column(Text, default="")
    source_filename: Mapped[str] = mapped_column(String(255), default="")
    status: Mapped[str] = mapped_column(String(20), default="OPEN")  # OPEN | STOPPED
    requirements_confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    confirmed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_by: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    requirements: Mapped[list["Requirement"]] = relationship(
        back_populates="job", cascade="all, delete-orphan", order_by="Requirement.id"
    )


class Requirement(Base):
    __tablename__ = "job_requirements"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id", ondelete="CASCADE"), index=True)
    category: Mapped[str] = mapped_column(String(20))  # skill | education | experience
    text_original: Mapped[str] = mapped_column(Text)  # JD ke asli alfaz, kabhi change nahi
    text_normalized: Mapped[str] = mapped_column(Text)  # recruiter edit kar sakta hai
    mandatory: Mapped[bool] = mapped_column(Boolean, default=True)
    min_years: Mapped[int | None] = mapped_column(Integer, nullable=True)
    job: Mapped[Job] = relationship(back_populates="requirements")
