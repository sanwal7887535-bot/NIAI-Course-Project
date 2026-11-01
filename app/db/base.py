import importlib
import pkgutil

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


def import_all_models() -> None:
    """Har module ki models.py import karta hai taake Alembic aur SQLAlchemy sab tables dekh sakein.

    Models `Base` isi file se import karte hain, is liye yahan se models import karna circular
    hota; function ke andar karna safe hai. Naya module aaye to kuch badalna nahi parta.
    """
    import app.modules as modules_pkg

    for mod in pkgutil.iter_modules(modules_pkg.__path__):
        try:
            importlib.import_module(f"app.modules.{mod.name}.models")
        except ModuleNotFoundError as e:
            if e.name != f"app.modules.{mod.name}.models":
                raise  # models.py hai magar uski apni import toot gayi - chhupana nahi
