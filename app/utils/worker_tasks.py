from celery_worker import app
from .data_transaction import (
    transfer_category_data,
    transfer_school_data,
    transfer_total_enrolled_data,
    transfer_gender_enrolled_data,
    transfer_grade_enrolled_data,
    transfer_race_enrolled_data
)
import pandas as pd
from fastapi.encoders import jsonable_encoder
import plotly.graph_objects as go
from .chart import _create_chart
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
    
    
    
@app.task(name="create_chart")
def create_chart(_type, json_data):
        _create_chart(_type, json_data)