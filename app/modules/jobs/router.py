import os
import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.permissions import require_role
from app.db.session import get_db
from . import service
from .schemas import ConfirmRequest, JobOut, RequirementOut

router = APIRouter(prefix="/jobs", tags=["jobs"])
recruiter = require_role("recruiter", "admin")

JD_EXT = {".pdf", ".docx"}
JD_MAX = 10 * 1024 * 1024


def _job_out(j) -> JobOut:
    return JobOut(id=j.id, title=j.title, status=j.status,
                  requirements_confirmed=j.requirements_confirmed)


@router.post("", response_model=JobOut)  # NOTE: contract table mein nahi, teeno members se approve karwayein
async def create_job(file: UploadFile = File(...), db: Session = Depends(get_db),
                     user=Depends(recruiter)):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in JD_EXT:
        raise HTTPException(415, "Only PDF or DOCX allowed")
    data = await file.read()
    if len(data) > JD_MAX:
        raise HTTPException(413, "File too large")
    os.makedirs("storage/uploads/jd", exist_ok=True)
    path = f"storage/uploads/jd/{uuid.uuid4().hex}{ext}"
    with open(path, "wb") as f:
        f.write(data)
    job = service.create_job_from_file(db, path, os.path.basename(file.filename), user.id)
    return _job_out(job)


@router.get("", response_model=list[JobOut])
def list_jobs(db: Session = Depends(get_db), _=Depends(recruiter)):
    return service.list_jobs(db)


@router.get("/{job_id}/requirements", response_model=list[RequirementOut])
def get_requirements(job_id: int, db: Session = Depends(get_db), _=Depends(recruiter)):
    return service.get_job(db, job_id).requirements


@router.post("/{job_id}/requirements/confirm", response_model=list[RequirementOut])
def confirm(job_id: int, body: ConfirmRequest, db: Session = Depends(get_db), _=Depends(recruiter)):
    return service.confirm_requirements(db, job_id, body.requirements).requirements


@router.post("/{job_id}/stop", response_model=JobOut)
def stop(job_id: int, db: Session = Depends(get_db), _=Depends(recruiter)):
    return _job_out(service.stop_job(db, job_id))
