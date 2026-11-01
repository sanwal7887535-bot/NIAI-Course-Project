from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from .models import User


def authenticate(db: Session, email: str, password: str) -> User | None:
    user = db.scalar(select(User).where(User.email == email.lower().strip()))
    if user and user.is_active and verify_password(password, user.password_hash):
        return user
    return None


def login(db: Session, email: str, password: str):
    user = authenticate(db, email, password)
    if not user:
        return None
    return create_access_token(user.id, user.role), user
