import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    BASE_DIR / "data" / "cleaned" / "superstore_final.csv"
)

st.title("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", f"${df['Sales'].sum():,.0f}")
col2.metric("Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Orders", df["Order ID"].nunique())
col4.metric("Customers", df["Customer ID"].nunique())

monthly = (
    df.groupby("Order Month")["Sales"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly,
    x="Order Month",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)
