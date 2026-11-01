from pydantic import BaseModel

from app.ai.llm.client import complete_json  # ASSUMPTION: apne LLM client ka function naam


class ReqItem(BaseModel):
    category: str  # skill | education | experience
    text_original: str
    text_normalized: str
    mandatory: bool
    min_years: int | None = None


class JDResult(BaseModel):
    title: str
    requirements: list[ReqItem]


PROMPT = """Extract from this job description: the job title and a list of requirements.
Each requirement has: category (skill|education|experience), text_original (copy the exact
words from the JD), text_normalized (short clean form), mandatory (true only if the JD says
must/required; "preferred/plus/nice to have" = false), min_years (integer only if stated, else null).
Never invent requirements. If unsure, leave null.
Return JSON only: {{"title": str, "requirements": [ ... ]}}

JOB DESCRIPTION:
{text}"""


def extract_requirements(text: str) -> JDResult:
    raw = complete_json(PROMPT.format(text=text[:12000]))
    return JDResult.model_validate(raw)
