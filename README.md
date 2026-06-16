# AI-Powered E-Commerce Sales Forecasting & Customer Analytics Platform

## Overview
This project is an end-to-end AI-powered E-Commerce Sales Forecasting and Customer Analytics Platform developed using Python, Machine Learning, Power BI, and Streamlit. The project analyzes historical sales data, identifies customer segments using RFM Analysis and K-Means Clustering, forecasts future sales trends, and presents business insights through interactive dashboards.

The platform helps businesses understand customer behavior, monitor sales performance, identify high-value customers, and make data-driven decisions. It combines data cleaning, exploratory data analysis, SQL-based business analytics, machine learning models, Power BI dashboards, and a Streamlit web application into a single analytics solution.



## Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* SQL-Based Business Analysis
* Customer Segmentation using RFM Analysis
* K-Means Clustering for Customer Groups
* Sales Forecasting using Machine Learning
* Interactive Power BI Dashboards
* Streamlit Web Application
* Business Insights and Performance Tracking
* Future Sales Prediction for Strategic Planning



## Tech Stack

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-Learn
* K-Means Clustering
* Linear Regression
* Random Forest Regressor

### Business Intelligence

* Power BI

### Web Application

* Streamlit

### Database & Querying

* SQL
* SQLite

### Model Storage

* Joblib

### Version Control

* Git
* GitHub


## Project Structure

```text
AI-Powered-ECommerce-Sales-Forecasting-Customer-Analytics
│
├── data
│   ├── raw
│   │   └── superstore_clean.xls
│   └── cleaned
│       ├── superstore_clean.csv
│       └── superstore_final.csv
│
├── notebook
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_sql_analysis.ipynb
│   ├── 04_rfm_segmentation.ipynb
│   └── 05_sales_forecasting.ipynb
│
├── app
│   ├── streamlit_app.py
│   └── pages
│       ├── 1_Executive_Overview.py
│       ├── 2_Sales_Analytics.py
│       ├── 3_Customer_Segmentation.py
│       └── 4_Sales_Forecast.py
│
├── exports
│   ├── eda_insights.txt
│   ├── rfm_segments.csv
│   └── monthly_forecast.csv
│
├── models
│   ├── rfm_kmeans.pkl
│   ├── rfm_scaler.pkl
│   └── sales_forecast_rf.pkl
│
├── powerbi
│   ├── sales_dashboard.pbix
│   └── screenshots
│       ├── executive_dashboard.png
│       ├── sales_dashboard.png
│       ├── customer_dashboard.png
│       └── forecast_dashboard.png
│
├── reports
│   └── PowerBI_Dashboard_Report.pdf
│
├── assets
│   └── screenshots
│       ├── executive_dashboard.png
│       ├── sales_dashboard.png
│       ├── customer_dashboard.png
│       └── forecast_dashboard.png
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```


## Dashboard Screenshots

### Executive Dashboard
<img width="1282" height="720" alt="executive_dashboard" src="https://github.com/user-attachments/assets/67901ff8-005a-47ac-a107-d3672d3acf3c" />

### Sales Analytics Dashboard
<img width="1282" height="722" alt="sales_dashboard" src="https://github.com/user-attachments/assets/54b4dd0a-164a-4361-bfc1-fe59873f567f" />

### Customer Segmentation Dashboard
<img width="1280" height="720" alt="customer_dashboard" src="https://github.com/user-attachments/assets/c94269ab-a76b-4de2-9231-da14fc52ed6f" />

### Sales Forecast Dashboard
<img width="1278" height="718" alt="forecast_dashboard" src="https://github.com/user-attachments/assets/e7fd767a-79e1-49b8-aa93-872b086a7dfe" />


## Future Improvements

- Deploy Streamlit application on Streamlit Cloud
- Add real-time sales data integration
- Implement advanced forecasting models (XGBoost, Prophet)
- Add customer churn prediction
- Build recommendation system for products
- Integrate SQL database instead of CSV files
- Enhance dashboard UI/UX
- Add role-based authentication
- Create mobile-friendly dashboard
