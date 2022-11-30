import importlib

from django.apps import AppConfig
from django.contrib import admin


class BaseAppConfig(AppConfig):
    """Base AppConfig for UvU apps."""

    def ready(self):
        # Dynamically import the signals submodule inside ready().
        try:
            importlib.import_module(".signals", f"{self.name}")
        except ModuleNotFoundError:
            pass
