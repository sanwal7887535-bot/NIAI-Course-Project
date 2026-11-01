"""Tests sqlite in-memory par chalte hain; Postgres, Redis, LLM ki zaroorat nahi."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.security import hash_password
from app.db.base import Base, import_all_models
from app.db.session import get_db
from app.main import app as fastapi_app
from app.modules.auth.models import User

PASSWORD = "ChangeMe123!"
PDF = b"%PDF-1.4\n" + b"fake cv content " * 20


@pytest.fixture()
def db_session(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)  # storage/uploads tmp mein bane
    import_all_models()
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False},
                           poolclass=StaticPool)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    with Session() as s:
        for email, role in [("recruiter@example.com", "recruiter"),
                            ("reviewer@example.com", "reviewer")]:
            s.add(User(email=email, name=role, role=role, password_hash=hash_password(PASSWORD)))
        s.commit()

    def override():
        db = Session()
        try:
            yield db
        finally:
            db.close()

    fastapi_app.dependency_overrides[get_db] = override
    yield Session
    fastapi_app.dependency_overrides.clear()


@pytest.fixture()
def client(db_session):
    return TestClient(fastapi_app)


def _token(client, email):
    r = client.post("/auth/login", json={"email": email, "password": PASSWORD})
    assert r.status_code == 200, r.text
    return r.json()["token"]


@pytest.fixture()
def recruiter_headers(client):
    return {"Authorization": f"Bearer {_token(client, 'recruiter@example.com')}"}


@pytest.fixture()
def reviewer_headers(client):
    return {"Authorization": f"Bearer {_token(client, 'reviewer@example.com')}"}


@pytest.fixture()
def parse_calls(monkeypatch):
    """Celery/LLM/OCR ki jagah fake; parse_cv.delay ke calls record karta hai."""
    from app.ai.extraction.jd_extractor import JDResult, ReqItem
    import app.workers.tasks.parse_cv as pc

    monkeypatch.setattr("app.modules.jobs.service.extract_text", lambda p: "job description " * 20)
    monkeypatch.setattr(
        "app.modules.jobs.service.extract_requirements",
        lambda t: JDResult(title="Backend Engineer", requirements=[
            ReqItem(category="skill", text_original="Must know Python",
                    text_normalized="Python", mandatory=True),
            ReqItem(category="experience", text_original="3+ years of backend work",
                    text_normalized="Backend experience", mandatory=True, min_years=3),
            ReqItem(category="skill", text_original="Docker is a plus",
                    text_normalized="Docker", mandatory=False),
        ]))
    calls = []
    monkeypatch.setattr(pc.parse_cv, "delay", lambda application_id: calls.append(application_id))
    return calls
