import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

forecast = pd.read_csv(
    BASE_DIR / "exports" / "monthly_forecast.csv"
)

st.title("Sales Forecast")

st.metric(
    "Average Forecast Sales",
    round(
        forecast["Predicted_Sales"].mean()
    )
)

fig = px.line(
    forecast,
    x="Month_Index",
    y="Predicted_Sales",
    title="Future Sales Forecast"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(forecast)
