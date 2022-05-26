from celery_worker import app
from .data_transaction import (
    transfer_category_data,
    transfer_school_data,
    transfer_total_enrolled_data,
    transfer_gender_enrolled_data,
    transfer_grade_enrolled_data,
    transfer_race_enrolled_data
)
import time

# a dummy task
@app.task(name="create_task")
def create_task(a,b,c):
    time.sleep(a)
    return b + c


'''
Transfer data: csv -> DB
'''
@app.task(name="load_csv_data")
def load_csv_data():
    transfer_category_data()
    transfer_school_data()
    transfer_total_enrolled_data()
    transfer_gender_enrolled_data()
    transfer_grade_enrolled_data()
    transfer_race_enrolled_data()