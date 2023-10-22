from __future__ import absolute_import

import os

from celery import Celery
from Django_Portfolio import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_Portfolio.settings")

app = Celery("Django_Portfolio")

app.config_from_object("Django_Portfolio.settings", namespace="CELERY"),

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)