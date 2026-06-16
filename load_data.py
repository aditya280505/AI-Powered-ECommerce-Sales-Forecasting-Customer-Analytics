import pandas as pd

def load_sales_data():
    return pd.read_csv("data/cleaned/superstore_final.csv")

def load_rfm():
    return pd.read_csv("exports/rfm_segments.csv")

def load_forecast():
    return pd.read_csv("exports/monthly_forecast.csv")