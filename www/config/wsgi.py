"""
WSGI config for clinic project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.config.settings.prod")

#os.environ["DJANGO_SETTINGS_MODULE"] = "www.config.settings.prod"

application = get_wsgi_application()
