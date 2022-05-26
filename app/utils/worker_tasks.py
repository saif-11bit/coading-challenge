from celery_worker import app
import time

# a dummy task
@app.task(name="create_task")
def create_task(a,b,c):
    time.sleep(a)
    return b + c