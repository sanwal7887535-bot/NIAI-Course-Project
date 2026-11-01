from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.modules.candidates.models import Candidate
from app.modules.documents import service as docs
from app.modules.jobs.service import get_job
from .models import Application

NOTICE_VERSION = getattr(settings, "CONSENT_NOTICE_VERSION", "v1")  # config.py mein add-only setting


async def create_application(
    db: Session, *, job_id: int, full_name: str, email: str, phone: str, linkedin_url: str,
    referee_name: str, referee_email: str, referee_company: str,
    consent_verification: bool, consent_current_employer: bool, cv: UploadFile,
) -> Application:
    job = get_job(db, job_id)
    if job.status != "OPEN" or not job.requirements_confirmed:
        raise HTTPException(409, "This job is not accepting applications")
    if not consent_verification:
        raise HTTPException(422, "Consent to verification is required to apply")
    email = email.lower().strip()
    dup = (db.query(Application).join(Candidate, Candidate.id == Application.candidate_id)
           .filter(Application.job_id == job_id, Candidate.email == email).first())
    if dup:
        raise HTTPException(409, "You have already applied for this job")
    try:
        cand = Candidate(full_name=full_name.strip(), email=email, phone=phone, linkedin_url=linkedin_url)
        db.add(cand)
        db.flush()
        app = Application(
            job_id=job_id, candidate_id=cand.id, stage="APPLIED",
            referee_name=referee_name, referee_email=referee_email.lower().strip(),
            referee_company=referee_company,
            consent_verification=consent_verification,
            consent_current_employer=consent_current_employer,
            consent_notice_version=NOTICE_VERSION,
        )
        db.add(app)
        db.flush()
        await docs.save_upload(db, app.id, cv, "CV")
        db.commit()
    except Exception:
        db.rollback()
        raise
    from app.workers.tasks.parse_cv import parse_cv  # commit ke BAAD, warna worker ko row nahi milegi

    parse_cv.delay(app.id)
    return app


def get_consent(db: Session, application_id: int) -> dict:  # Member 2 ke liye (frozen contract)
    a = db.get(Application, application_id)
    if not a:
        raise HTTPException(404, "Application not found")
    return {"verification": a.consent_verification,
            "current_employer": a.consent_current_employer,
            "given_at": a.consent_at,
            "notice_version": a.consent_notice_version}
