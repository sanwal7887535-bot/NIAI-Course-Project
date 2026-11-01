from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.db.session import get_db
from . import service

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", status_code=201)  # public (candidate)
async def apply(
    job_id: int = Form(...), full_name: str = Form(...), email: str = Form(...),
    phone: str = Form(""), linkedin_url: str = Form(""),
    referee_name: str = Form(""), referee_email: str = Form(""), referee_company: str = Form(""),
    consent_verification: bool = Form(False), consent_current_employer: bool = Form(False),
    cv: UploadFile = File(...), db: Session = Depends(get_db),
):
    app = await service.create_application(
        db, job_id=job_id, full_name=full_name, email=email, phone=phone,
        linkedin_url=linkedin_url, referee_name=referee_name, referee_email=referee_email,
        referee_company=referee_company, consent_verification=consent_verification,
        consent_current_employer=consent_current_employer, cv=cv)
    return {"application_id": app.id, "stage": app.stage}
