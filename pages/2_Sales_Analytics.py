import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    BASE_DIR / "data" / "cleaned" / "superstore_final.csv"
)

st.title("Sales Analytics")

category = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig, use_container_width=True)

region = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region,
    names="Region",
    values="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig2, use_container_width=True)
