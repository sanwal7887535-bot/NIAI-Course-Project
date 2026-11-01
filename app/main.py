"""App entry point. Sprint 0 mein ek baar likhi gayi; iske baad koi edit nahi karta.

Har `app/modules/<name>/router.py` aur `public_router.py` khud-ba-khud include hote hain,
is liye naye module ke liye yahan kuch nahi badalna.
"""
import importlib
import importlib.util
import pkgutil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.modules as modules_pkg
from app.core.config import settings
from app.db.base import import_all_models

ROUTER_FILES = ("router", "public_router")
ROUTER_ATTRS = ("router", "public_router")


def _cors_origins() -> list[str]:
    value = getattr(settings, "CORS_ORIGINS", None)
    if not value:
        return ["http://localhost:5173"]  # Vite default
    if isinstance(value, str):
        return [v.strip() for v in value.split(",") if v.strip()]
    return list(value)


def create_app() -> FastAPI:
    import_all_models()
    api = FastAPI(title="AI-Shortlisting")
    api.add_middleware(
        CORSMiddleware,
        allow_origins=_cors_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @api.get("/health", tags=["health"])
    def health():
        return {"status": "ok"}

    for mod in sorted(pkgutil.iter_modules(modules_pkg.__path__), key=lambda m: m.name):
        for fname in ROUTER_FILES:
            dotted = f"app.modules.{mod.name}.{fname}"
            if importlib.util.find_spec(dotted) is None:
                continue
            module = importlib.import_module(dotted)
            for attr in ROUTER_ATTRS:
                router = getattr(module, attr, None)
                if router is not None:
                    api.include_router(router)
                    break
    return api


app = create_app()
