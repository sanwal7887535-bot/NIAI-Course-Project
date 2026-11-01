"""Member 3 uploaded files isi module se parhega (get_files)."""
import os
import uuid

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from .models import Document

ALLOWED = {
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}
MAGIC = {".pdf": b"%PDF", ".docx": b"PK"}
MAX_BYTES = 5 * 1024 * 1024


async def save_upload(db: Session, application_id: int, file: UploadFile, kind: str = "CV") -> Document:
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED:
        raise HTTPException(415, "Only PDF or DOCX files are allowed")
    data = await file.read()
    if len(data) > MAX_BYTES:
        raise HTTPException(413, "File too large (max 5 MB)")
    if not data.startswith(MAGIC[ext]):
        raise HTTPException(415, "File content does not match its extension")
    os.makedirs("storage/uploads", exist_ok=True)
    path = f"storage/uploads/{uuid.uuid4().hex}{ext}"  # asli filename kabhi use nahi karte
    with open(path, "wb") as f:
        f.write(data)
    doc = Document(application_id=application_id, kind=kind, stored_path=path,
                   original_name=os.path.basename(file.filename), mime_type=ALLOWED[ext],
                   size_bytes=len(data))
    db.add(doc)
    db.flush()
    return doc


def get_files(db: Session, application_id: int, kind: str | None = None) -> list[Document]:
    q = db.query(Document).filter_by(application_id=application_id)
    return q.filter_by(kind=kind).all() if kind else q.all()
