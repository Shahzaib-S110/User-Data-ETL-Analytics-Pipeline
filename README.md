# 📊 User Data ETL & Analytics Pipeline (PostgreSQL + Streamlit)

A complete end-to-end **Data Engineering + Analytics project** that extracts user data from an API, transforms it into a structured model, loads it into PostgreSQL, and visualizes insights using a Streamlit dashboard.

---

## 🚀 Overview

This project demonstrates a full **ETL pipeline + BI dashboard system**:

- Extract data from DummyJSON API
- Transform & clean using Pandas
- Load into PostgreSQL (relational schema)
- Run SQL-based OLAP analytics
- Visualize insights using Streamlit + Plotly

---

## 🏗️ Architecture

API (DummyJSON)
↓
Extract (Requests)
↓
Transform (Pandas)
↓
PostgreSQL (Data Warehouse)
↓
SQL Analytics (OLAP Queries)
↓
Streamlit Dashboard
---

## ⚙️ Tech Stack

- Python
- PostgreSQL
- Pandas
- SQLAlchemy
- Streamlit
- Plotly
- Seaborn (EDA)

---

## 📁 Project Structure


User-Data-ETL-Analytics-Pipeline/
│
├── src/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── schema.py
│ ├── database.py
│ └── main.py
│
├── dashboard/
│ ├── app.py
│ ├── database.py
│ ├── queries.py
│ ├── charts.py
│ ├── utils.py
│ └── pages/
│
├── requirements.txt
└── README.md



---

## 🔄 ETL Pipeline

### 1. Extract
- Fetch data from API (DummyJSON)
- Handle pagination
- Store raw JSON

### 2. Transform
- Clean missing values
- Standardize text fields
- Feature engineering:
  - Age groups
  - BMI calculation
  - Email domain extraction

### 3. Load
- Load structured data into PostgreSQL tables:
  - users
  - addresses
  - companies
  - bank
  - crypto
  - devices
  - hair

---

## 📊 Analytics (SQL / OLAP)

- GROUP BY aggregations
- JOIN operations
- CTE queries
- Data segmentation
- Ranking & filtering

Example:

```sql
SELECT gender, COUNT(*)
FROM users
GROUP BY gender;

## 📁 Project Structure
