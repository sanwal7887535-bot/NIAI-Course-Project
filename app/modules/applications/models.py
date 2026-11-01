from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), index=True)
    candidate_id: Mapped[int] = mapped_column(ForeignKey("candidates.id"), index=True)
    stage: Mapped[str] = mapped_column(String(20), default="APPLIED")  # TODO: core/enums.py ka stage enum
    match_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    referee_name: Mapped[str] = mapped_column(String(255), default="")
    referee_email: Mapped[str] = mapped_column(String(255), default="")
    referee_company: Mapped[str] = mapped_column(String(255), default="")
    consent_verification: Mapped[bool] = mapped_column(Boolean, default=False)
    consent_current_employer: Mapped[bool] = mapped_column(Boolean, default=False)  # alag flag
    consent_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    consent_notice_version: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
