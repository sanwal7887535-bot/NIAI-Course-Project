from app.workers.celery_app import celery_app


@celery_app.task(name="parse_cv")
def parse_cv(application_id: int):
    """Task 5 (Sprint 2) mein poora hoga: text -> OCR fallback -> cv_extractor -> stage PARSED."""
    return {"application_id": application_id, "status": "stub"}
