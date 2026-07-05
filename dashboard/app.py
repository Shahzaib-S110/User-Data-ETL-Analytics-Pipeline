import streamlit as st

from database import test_connection
from utils import (
    configure_page,
    load_css,
    sidebar,
    page_title,
    footer,
    info,
    warning
)

# ==========================================================
# INIT APP
# ==========================================================

configure_page()
load_css()

# ==========================================================
# SIDEBAR
# ==========================================================

sidebar()

# ==========================================================
# HEADER
# ==========================================================

page_title(
    "📊 User Data ETL Analytics Dashboard",
    "PostgreSQL + Streamlit + Plotly | End-to-End Data Engineering Project"
)

# ==========================================================
# DATABASE CONNECTION CHECK
# ==========================================================

st.subheader("🗄 Database Status")

if test_connection():
    st.success("✅ PostgreSQL Connected Successfully")
else:
    st.error("❌ Database Connection Failed")

    warning("Please check:\n"
            "- PostgreSQL is running\n"
            "- DB name is correct (user_etl_db)\n"
            "- Username/password in database.py")

    st.stop()

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.subheader("🚀 Project Overview")

st.markdown("""
This is a complete **ETL + Analytics Project**:

### 🔄 ETL Pipeline
1. Extract data from DummyJSON API
2. Transform nested JSON into relational tables
3. Load data into PostgreSQL

### 📊 Analytics Layer
- SQL-based analysis
- Aggregations (GROUP BY, COUNT, AVG)
- Joins across multiple tables

### 📈 Visualization Layer
- Streamlit dashboard
- Plotly interactive charts
- KPI cards and filters
""")

# ==========================================================
# DATA PIPELINE FLOW
# ==========================================================

st.subheader("⚙ ETL Pipeline Flow")

st.code("""
DummyJSON API
      │
      ▼
EXTRACT (requests)
      │
      ▼
TRANSFORM (pandas)
      │
      ▼
LOAD (PostgreSQL)
      │
      ▼
STREAMLIT DASHBOARD
""")

# ==========================================================
# DATABASE TABLES
# ==========================================================

st.subheader("🗄 Database Schema")

st.code("""
users
addresses
companies
company_addresses
bank
crypto
devices
hair
""")

# ==========================================================
# DASHBOARD FEATURES
# ==========================================================

st.subheader("📌 Dashboard Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### 👤 User Analytics
- Gender distribution
- Age distribution
- Age groups
- BMI analysis
- Height vs Weight
""")

    st.markdown("""
### 🌍 Geographic Analysis
- Users by country
- Top cities
- Interactive map
""")

with col2:

    st.markdown("""
### 💼 Company Analytics
- Departments
- Job titles
- Company distribution
""")

    st.markdown("""
### 💳 Financial Analytics
- Card types
- Currency usage
- Crypto distribution
""")

# ==========================================================
# TECH STACK
# ==========================================================

with st.expander("🧰 Tech Stack Used"):

    st.markdown("""
- Python 🐍
- PostgreSQL 🐘
- SQLAlchemy
- Pandas
- Streamlit
- Plotly
- ETL Pipeline Architecture
""")

# ==========================================================
# WHY THIS PROJECT IS IMPORTANT
# ==========================================================

with st.expander("💡 Why this project matters"):

    st.markdown("""
This project demonstrates:

✔ End-to-end data engineering pipeline  
✔ Real-world ETL architecture  
✔ SQL analytics skills (joins, aggregations)  
✔ Dashboard development skills  
✔ Data visualization expertise  
✔ Backend + analytics integration  

This is exactly what companies expect from:
- Data Analysts
- Data Engineers
- BI Developers
""")

# ==========================================================
# FOOTER
# ==========================================================

footer()