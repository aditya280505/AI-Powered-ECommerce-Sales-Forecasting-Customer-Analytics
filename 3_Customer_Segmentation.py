import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

rfm = pd.read_csv(
    BASE_DIR / "exports" / "rfm_segments.csv"
)

st.title("Customer Segmentation")

st.metric(
    "Total Customers",
    rfm.shape[0]
)

segment_counts = (
    rfm["Segment"]
    .value_counts()
)

st.bar_chart(segment_counts)

fig = px.scatter(
    rfm,
    x="Recency",
    y="Monetary",
    color="Segment"
)

st.plotly_chart(fig, use_container_width=True)
