import importlib
from typing import Optional
from types import ModuleType

__all__ = ["import_package"]


def import_package(package_name: str) -> Optional[ModuleType]:
    """
    Imports a package using importlib. Either the package or None is returned.
    """
    try:
        module = importlib.import_module(package_name)
        return module
    except ImportError:
        return None
