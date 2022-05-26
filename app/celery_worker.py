import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv(verbose=True)

CELERY_BROKER_URL=os.environ["CELERY_BROKER_URL"]

app = Celery()
app.conf.broker_url = CELERY_BROKER_URL
app.conf.result_backend = CELERY_BROKER_URL

app.autodiscover_tasks(['utils.worker_tasks.py',], force=True)