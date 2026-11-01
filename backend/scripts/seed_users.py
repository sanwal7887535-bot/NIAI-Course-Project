"""Run: python -m scripts.seed_users   (backend/ folder se)"""
from app.core.security import hash_password
from app.db.base import import_all_models
from app.db.session import SessionLocal
from app.modules.auth.models import User

SEED = [
    ("admin@example.com", "Admin", "admin"),
    ("recruiter@example.com", "Test Recruiter", "recruiter"),
    ("reviewer@example.com", "Test Reviewer", "reviewer"),
]

import_all_models()
db = SessionLocal()
for email, name, role in SEED:
    if not db.query(User).filter_by(email=email).first():
        db.add(User(email=email, name=name, role=role, password_hash=hash_password("ChangeMe123!")))
db.commit()
print("done - password: ChangeMe123! (sirf development ke liye)")
