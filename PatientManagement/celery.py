import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PatientManagement.settings")
app = Celery("PatientManagement")
app.config_from_object("django.conf:settings",namespace="CELERY")
