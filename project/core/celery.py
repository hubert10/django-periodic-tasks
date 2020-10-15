from __future__ import absolute_import
import os
from celery import Celery
from django.apps import apps
from core.tasks import sample_task
from celery.app.registry import TaskRegistry

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

# This line will tell Celery to autodiscover all your tasks.py that are in your app foldersapp
registration = TaskRegistry()
registration.register(sample_task)
