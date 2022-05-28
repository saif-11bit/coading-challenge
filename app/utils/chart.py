import pandas as pd
import plotly.graph_objects as go

def _create_chart(_type, json_data):
        df = pd.DataFrame(json_data)

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
        fig.write_image(f"static/{_type}.png")