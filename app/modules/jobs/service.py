from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.ai.extraction.jd_extractor import extract_requirements
from app.ai.parsing import extract_text  # ASSUMPTION: existing text extractor (path -> str)
from app.core.config import settings
from .models import Job, Requirement


def create_job_from_file(db: Session, path: str, filename: str, user_id: int) -> Job:
    text = extract_text(path)
    if len(text.strip()) < 50:
        raise HTTPException(422, "Could not read text from the job description")
    result = extract_requirements(text)
    job = Job(title=result.title or filename, description_text=text,
              source_filename=filename, created_by=user_id)
    job.requirements = [Requirement(**r.model_dump()) for r in result.requirements]
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_job(db: Session, job_id: int) -> Job:
    job = db.get(Job, job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job


def list_jobs(db: Session) -> list[dict]:
    from app.modules.applications.models import Application  # circular import se bachne ke liye

    threshold = getattr(settings, "SHORTLIST_THRESHOLD", 65)
    rows = []
    for job in db.scalars(select(Job).order_by(Job.id.desc())):
        total = db.scalar(select(func.count()).select_from(Application)
                          .where(Application.job_id == job.id)) or 0
        short = db.scalar(select(func.count()).select_from(Application)
                          .where(Application.job_id == job.id,
                                 Application.match_score >= threshold)) or 0
        rows.append({"id": job.id, "title": job.title, "status": job.status,
                     "requirements_confirmed": job.requirements_confirmed,
                     "applications_count": total, "shortlisted_count": short})
    return rows


def confirm_requirements(db: Session, job_id: int, items: list) -> Job:
    job = get_job(db, job_id)
    if job.status == "STOPPED":
        raise HTTPException(409, "Job is stopped")
    existing = {r.id: r for r in job.requirements}
    keep_ids: set[int] = set()
    new_rows: list[Requirement] = []
    for it in items:
        if it.id and it.id in existing:
            r = existing[it.id]
            r.category, r.text_normalized = it.category, it.text_normalized
            r.mandatory, r.min_years = it.mandatory, it.min_years  # text_original touch nahi
            keep_ids.add(r.id)
        else:
            new_rows.append(Requirement(
                category=it.category, text_original=it.text_original or it.text_normalized,
                text_normalized=it.text_normalized, mandatory=it.mandatory, min_years=it.min_years))
    job.requirements = [r for r in job.requirements if r.id in keep_ids] + new_rows
    job.requirements_confirmed = True
    job.confirmed_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(job)
    return job


def stop_job(db: Session, job_id: int) -> Job:
    job = get_job(db, job_id)
    job.status = "STOPPED"
    db.commit()
    db.refresh(job)
    return job


def is_job_stopped(db: Session, job_id: int) -> bool:  # Member 2 yeh call kar sakta hai
    return get_job(db, job_id).status == "STOPPED"


def assert_confirmed(db: Session, job_id: int) -> Job:  # matching (Task 6) yeh call karega
    job = get_job(db, job_id)
    if not job.requirements_confirmed:
        raise HTTPException(409, "Requirements not confirmed")
    if job.status == "STOPPED":
        raise HTTPException(409, "Job is stopped")
    return job
