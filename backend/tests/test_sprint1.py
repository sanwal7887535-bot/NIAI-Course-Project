from tests.conftest import PDF


def _create_job(client, headers):
    r = client.post("/jobs", headers=headers,
                    files={"file": ("jd.pdf", PDF, "application/pdf")})
    assert r.status_code == 200, r.text
    return r.json()["id"]


def _confirm(client, headers, job_id):
    reqs = client.get(f"/jobs/{job_id}/requirements", headers=headers).json()
    body = {"requirements": [dict(r) for r in reqs]}
    r = client.post(f"/jobs/{job_id}/requirements/confirm", headers=headers, json=body)
    assert r.status_code == 200, r.text
    return r.json()


def _apply(client, job_id, **over):
    data = {"job_id": job_id, "full_name": "Ali Khan", "email": "ali@example.com",
            "consent_verification": "true", "consent_current_employer": "false"}
    data.update(over)
    files = {"cv": ("cv.pdf", PDF, "application/pdf")}
    return client.post("/applications", data=data, files=files)


# ---------- Task 1: login ----------
def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_login_ok_and_bad_password(client):
    ok = client.post("/auth/login", json={"email": "Recruiter@Example.com", "password": "ChangeMe123!"})
    assert ok.status_code == 200
    assert ok.json()["user"]["role"] == "recruiter" and ok.json()["token"]
    bad = client.post("/auth/login", json={"email": "recruiter@example.com", "password": "nope"})
    assert bad.status_code == 401


def test_401_without_token_and_403_wrong_role(client, reviewer_headers):
    assert client.get("/jobs").status_code == 401
    assert client.get("/jobs", headers={"Authorization": "Bearer garbage"}).status_code == 401
    assert client.get("/jobs", headers=reviewer_headers).status_code == 403


# ---------- Task 2 + 3: jobs, confirm, stop ----------
def test_create_job_keeps_original_wording(client, recruiter_headers, parse_calls):
    job_id = _create_job(client, recruiter_headers)
    reqs = client.get(f"/jobs/{job_id}/requirements", headers=recruiter_headers).json()
    assert len(reqs) == 3
    assert reqs[0]["text_original"] == "Must know Python"
    assert reqs[2]["mandatory"] is False


def test_create_job_rejects_bad_extension(client, recruiter_headers):
    r = client.post("/jobs", headers=recruiter_headers,
                    files={"file": ("jd.exe", b"MZ", "application/octet-stream")})
    assert r.status_code == 415


def test_confirm_edits_normalized_but_never_original(client, recruiter_headers, parse_calls):
    job_id = _create_job(client, recruiter_headers)
    reqs = client.get(f"/jobs/{job_id}/requirements", headers=recruiter_headers).json()
    reqs[0]["text_normalized"] = "Python 3"
    reqs[0]["text_original"] = "TAMPERED"
    new = {"category": "education", "text_normalized": "BS Computer Science", "mandatory": True}
    body = {"requirements": [reqs[0], reqs[1], new]}  # reqs[2] hata di
    out = client.post(f"/jobs/{job_id}/requirements/confirm", headers=recruiter_headers, json=body).json()
    assert len(out) == 3
    assert out[0]["text_normalized"] == "Python 3" and out[0]["text_original"] == "Must know Python"
    assert any(r["text_original"] == "BS Computer Science" for r in out)
    listed = client.get("/jobs", headers=recruiter_headers).json()
    assert listed[0]["requirements_confirmed"] is True


def test_stop_job(client, recruiter_headers, parse_calls):
    job_id = _create_job(client, recruiter_headers)
    _confirm(client, recruiter_headers, job_id)
    assert client.post(f"/jobs/{job_id}/stop", headers=recruiter_headers).json()["status"] == "STOPPED"
    assert _apply(client, job_id).status_code == 409
    again = client.post(f"/jobs/{job_id}/requirements/confirm", headers=recruiter_headers,
                        json={"requirements": []})
    assert again.status_code == 409


# ---------- Task 4: apply ----------
def test_apply_blocked_until_confirmed(client, recruiter_headers, parse_calls):
    job_id = _create_job(client, recruiter_headers)
    assert _apply(client, job_id).status_code == 409


def test_apply_success_stores_file_and_consent(client, recruiter_headers, parse_calls, db_session):
    import os
    from app.modules.applications import service
    job_id = _create_job(client, recruiter_headers)
    _confirm(client, recruiter_headers, job_id)
    r = _apply(client, job_id, consent_current_employer="true")
    assert r.status_code == 201, r.text
    app_id = r.json()["application_id"]
    assert r.json()["stage"] == "APPLIED"
    assert parse_calls == [app_id]
    stored = os.listdir("storage/uploads")
    assert any(f.endswith(".pdf") for f in stored)
    assert all("cv.pdf" not in f for f in stored)  # asli filename use nahi hota
    with db_session() as s:
        consent = service.get_consent(s, app_id)
    assert consent["verification"] is True and consent["current_employer"] is True
    assert consent["notice_version"] and consent["given_at"]


def test_apply_rejections(client, recruiter_headers, parse_calls):
    job_id = _create_job(client, recruiter_headers)
    _confirm(client, recruiter_headers, job_id)
    assert _apply(client, job_id, consent_verification="false").status_code == 422
    exe = client.post("/applications", data={"job_id": job_id, "full_name": "A", "email": "a@x.com",
                      "consent_verification": "true"}, files={"cv": ("cv.exe", b"MZ", "application/octet-stream")})
    assert exe.status_code == 415
    fake_pdf = client.post("/applications", data={"job_id": job_id, "full_name": "A", "email": "a@x.com",
                           "consent_verification": "true"}, files={"cv": ("cv.pdf", b"not a pdf", "application/pdf")})
    assert fake_pdf.status_code == 415
    big = client.post("/applications", data={"job_id": job_id, "full_name": "A", "email": "a@x.com",
                      "consent_verification": "true"}, files={"cv": ("cv.pdf", b"%PDF" + b"0" * (6 * 1024 * 1024), "application/pdf")})
    assert big.status_code == 413
    assert parse_calls == []  # koi bhi reject hone par parse_cv start nahi hua


def test_duplicate_application_rejected(client, recruiter_headers, parse_calls):
    job_id = _create_job(client, recruiter_headers)
    _confirm(client, recruiter_headers, job_id)
    assert _apply(client, job_id).status_code == 201
    assert _apply(client, job_id).status_code == 409
