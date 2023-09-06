
# This file is required for Python to recognize the "apps" directory as a package.

from importlib import import_module
from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    name = "apps"

    def ready(self):
        import_module("apps.receivers")
