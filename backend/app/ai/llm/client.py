"""Shared LLM client (sab members use karte hain). Structured JSON output deta hai."""
import json
import re

from app.core.config import settings


def complete_text(prompt: str, system: str = "", max_tokens: int = 4000) -> str:
    import anthropic  # lazy import: tests ko package ki zaroorat na ho

    if not settings.ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY is not set in .env")
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    msg = client.messages.create(
        model=settings.LLM_MODEL,
        max_tokens=max_tokens,
        system=system or "You are a precise information extraction assistant. Never invent facts.",
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")


def parse_json_text(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.IGNORECASE)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start == -1 or end <= start:
            raise
        return json.loads(text[start:end + 1])


def complete_json(prompt: str, system: str = "", max_tokens: int = 4000) -> dict:
    return parse_json_text(complete_text(prompt, system, max_tokens))
