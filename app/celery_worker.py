import sys
import pathlib
sys.path.extend([str(pathlib.Path(__file__).parent.parent.absolute())])
import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv(verbose=True)

CELERY_BROKER_URL=os.environ["CELERY_BROKER_URL"]

celery = Celery()
celery.conf.broker_url = CELERY_BROKER_URL
celery.conf.result_backend = CELERY_BROKER_URL

celery.autodiscover_tasks(['app.utils.worker_tasks.py'], force=True)
