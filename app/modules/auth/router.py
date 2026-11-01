from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from . import service
from .schemas import LoginRequest, LoginResult

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginResult)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    result = service.login(db, body.email, body.password)
    if not result:
        raise HTTPException(401, "Invalid email or password")
    token, user = result
    return {"token": token, "user": user}
