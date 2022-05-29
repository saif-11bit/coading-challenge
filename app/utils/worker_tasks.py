from celery import shared_task
import pandas as pd
from fastapi.encoders import jsonable_encoder
import plotly.graph_objects as go
from app.utils.data_transaction import (
    transfer_category_data,
    transfer_school_data,
    transfer_total_enrolled_data,
    transfer_gender_enrolled_data,
    transfer_grade_enrolled_data,
    transfer_race_enrolled_data
)
from app.utils.data_transaction import (
    add_chart_data
)
'''
Transfer data: csv -> DB
'''
@shared_task(name="load_csv_data")
def load_csv_data():
    transfer_category_data()
    transfer_school_data()
    transfer_total_enrolled_data()
    transfer_gender_enrolled_data()
    transfer_grade_enrolled_data()
    transfer_race_enrolled_data()
    
    
'''
Create Chart
'''
@shared_task(name="create_chart")
def create_chart(chart_uuid, _type, json_data):
    
    df = pd.DataFrame(json_data)
    data = df.groupby(['category_id'])['count'].mean()
    chart_data = jsonable_encoder(data)
    chart_id = add_chart_data(chart_uuid, chart_data, _type)
    # 
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df["category_id"],
        y=df["count"]
    ))
    fig.update_layout(
        autosize=False,
        width=1000,
        height=700,
        yaxis=dict(
            title_text=f"{_type}",
            titlefont=dict(size=24),
        ),
        xaxis=dict(
            title_text="Categories",
            titlefont=dict(size=24),
        ),        
        
    )
    fig.write_image(f"static/{chart_uuid}.png")

    
