from pydantic import BaseModel


class RequirementOut(BaseModel):
    id: int
    category: str
    text_original: str
    text_normalized: str
    mandatory: bool
    min_years: int | None
    model_config = {"from_attributes": True}


class RequirementIn(BaseModel):
    id: int | None = None  # None = recruiter ne nayi requirement add ki
    category: str
    text_original: str = ""
    text_normalized: str
    mandatory: bool
    min_years: int | None = None


class ConfirmRequest(BaseModel):
    requirements: list[RequirementIn]


class JobOut(BaseModel):  # frontend ke features/jobs types se match karein
    id: int
    title: str
    status: str
    requirements_confirmed: bool
    applications_count: int = 0
    shortlisted_count: int = 0
