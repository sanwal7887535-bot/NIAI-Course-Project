"""users, jobs, job_requirements, candidates, applications, documents

Revision ID: 0001
Revises:
Create Date: 2026-11-01

NOTE: Sprint 0 task 7 mein teeno members ke tables agree hote hain. Agar Member 2/3 ki
migration pehle merge ho gayi ho to `down_revision` un ke revision par set karein (ek hi head).
"""
import sqlalchemy as sa
from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def _created_at():
    return sa.Column("created_at", sa.DateTime(timezone=True),
                     server_default=sa.func.now(), nullable=False)


def upgrade() -> None:
    bind = op.get_bind()
    if bind.dialect.name == "postgresql":
        op.execute("CREATE EXTENSION IF NOT EXISTS vector")  # pgvector (matching ke liye)

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("name", sa.String(120), nullable=False),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        _created_at(),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description_text", sa.Text(), nullable=False),
        sa.Column("source_filename", sa.String(255), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("requirements_confirmed", sa.Boolean(), nullable=False),
        sa.Column("confirmed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by", sa.Integer(), sa.ForeignKey("users.id"), nullable=True),
        _created_at(),
    )

    op.create_table(
        "job_requirements",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("job_id", sa.Integer(), sa.ForeignKey("jobs.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column("category", sa.String(20), nullable=False),
        sa.Column("text_original", sa.Text(), nullable=False),
        sa.Column("text_normalized", sa.Text(), nullable=False),
        sa.Column("mandatory", sa.Boolean(), nullable=False),
        sa.Column("min_years", sa.Integer(), nullable=True),
    )
    op.create_index("ix_job_requirements_job_id", "job_requirements", ["job_id"])

    op.create_table(
        "candidates",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("full_name", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("phone", sa.String(50), nullable=False),
        sa.Column("linkedin_url", sa.String(500), nullable=False),
        _created_at(),
    )
    op.create_index("ix_candidates_email", "candidates", ["email"])

    op.create_table(
        "applications",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("job_id", sa.Integer(), sa.ForeignKey("jobs.id"), nullable=False),
        sa.Column("candidate_id", sa.Integer(), sa.ForeignKey("candidates.id"), nullable=False),
        sa.Column("stage", sa.String(20), nullable=False),
        sa.Column("match_score", sa.Float(), nullable=True),
        sa.Column("referee_name", sa.String(255), nullable=False),
        sa.Column("referee_email", sa.String(255), nullable=False),
        sa.Column("referee_company", sa.String(255), nullable=False),
        sa.Column("consent_verification", sa.Boolean(), nullable=False),
        sa.Column("consent_current_employer", sa.Boolean(), nullable=False),
        sa.Column("consent_at", sa.DateTime(timezone=True), server_default=sa.func.now(),
                  nullable=False),
        sa.Column("consent_notice_version", sa.String(20), nullable=False),
        _created_at(),
    )
    op.create_index("ix_applications_job_id", "applications", ["job_id"])
    op.create_index("ix_applications_candidate_id", "applications", ["candidate_id"])

    op.create_table(
        "documents",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("application_id", sa.Integer(), sa.ForeignKey("applications.id"),
                  nullable=False),
        sa.Column("kind", sa.String(30), nullable=False),
        sa.Column("stored_path", sa.String(500), nullable=False),
        sa.Column("original_name", sa.String(255), nullable=False),
        sa.Column("mime_type", sa.String(100), nullable=False),
        sa.Column("size_bytes", sa.Integer(), nullable=False),
        _created_at(),
    )
    op.create_index("ix_documents_application_id", "documents", ["application_id"])


def downgrade() -> None:
    for table in ("documents", "applications", "candidates", "job_requirements", "jobs", "users"):
        op.drop_table(table)
