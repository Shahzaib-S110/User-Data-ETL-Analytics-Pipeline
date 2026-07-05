📊 User Data ETL & Analytics Pipeline (PostgreSQL + Streamlit BI Dashboard)

🚀 Project Overview

This project is a complete end-to-end Data Engineering + Analytics system that demonstrates how raw API data can be transformed into a professional BI dashboard using:

Extract → Transform → Load (ETL) pipeline
PostgreSQL data warehouse
SQL-based OLAP analytics
Streamlit interactive dashboard
Plotly visualizations

The dataset is fetched from DummyJSON API and transformed into a structured analytical model.

🏗️ Architecture
📡 DummyJSON API
        ↓
📥 Extract (Python Requests)
        ↓
🧹 Transform (Pandas)
        ↓
🗄️ Load (PostgreSQL)
        ↓
📊 SQL Analytics Layer (OLAP Queries)
        ↓
📈 Streamlit Dashboard (Plotly Visuals)
⚙️ Tech Stack
Python 🐍
PostgreSQL 🐘
Pandas 📊
SQLAlchemy 🔗
Streamlit 🚀
Plotly 📈
Seaborn (optional EDA)
Requests 🌐
📂 Project Structure
User-Data-ETL-Analytics-Pipeline/
│
├── src/
│   ├── extract.py         # API Data Extraction
│   ├── transform.py       # Data Cleaning & Feature Engineering
│   ├── load.py            # Load into PostgreSQL
│   ├── schema.py          # Database Schema (Tables)
│   ├── database.py        # DB Connection
│   └── main.py           # ETL Pipeline Runner
│
├── dashboard/
│   ├── app.py             # Streamlit Main App
│   ├── pages/            # Multi-page dashboard
│   ├── charts.py         # Plotly visualizations
│   ├── queries.py        # SQL queries (OLAP)
│   ├── utils.py         # Helper functions
│   └── database.py      # DB connection for dashboard
│
├── plots/                # Visualization outputs (optional)
├── requirements.txt
└── README.md
🔄 ETL Workflow
1️⃣ Extract
Fetches data from DummyJSON API
Handles pagination (limit & skip)
Stores raw JSON locally
2️⃣ Transform
Cleans missing values
Standardizes text fields
Feature engineering:
Age groups
BMI calculation
Email domain extraction
Normalizes nested JSON into relational structure
3️⃣ Load
Loads structured data into PostgreSQL
Creates relational tables:
users
addresses
companies
bank
crypto
devices
hair
📊 Analytics Layer (SQL OLAP)

This project uses advanced SQL:

GROUP BY aggregations
JOIN-based analytics
Window functions (optional extension)
CTEs (Common Table Expressions)
Analytical segmentation

Example:

SELECT gender, COUNT(*) 
FROM users
GROUP BY gender;
📈 Dashboard Features (Streamlit)
🏠 Home Dashboard
KPI metrics
Gender distribution
Country insights
Top cities
👤 User Analytics
Age distribution
Age vs Height
Age vs Weight
Demographic segmentation
🌍 Geographic Analytics
Country-wise users
City rankings
Interactive map (lat/lng)
💼 Company Analytics
Departments distribution
Job roles analysis
Company insights
💳 Finance Analytics
Bank card types
Currency usage
Crypto adoption
📄 Raw Data Explorer
SQL query runner
Table browser
Export CSV
Data quality checks
📊 Sample Visualizations
Bar Charts (categorical comparison)
Pie Charts (distribution)
Scatter Plots (relationships)
Maps (geospatial analysis)
Histograms (distribution analysis)
🚀 How to Run
1️⃣ Clone repository
git clone https://github.com/YOUR_USERNAME/User-Data-ETL-Analytics-Pipeline.git
cd User-Data-ETL-Analytics-Pipeline
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Setup PostgreSQL

Create database:

CREATE DATABASE user_etl_db;

Update credentials in:

src/config.py
dashboard/database.py
4️⃣ Run ETL pipeline
python src/main.py
5️⃣ Launch Dashboard
streamlit run dashboard/app.py
📌 Key Concepts Demonstrated
ETL Pipeline Design
Data Warehousing (PostgreSQL)
OLAP Analytical Queries
Star Schema Thinking
Data Cleaning & Feature Engineering
BI Dashboard Development
Interactive Data Visualization
🔥 Real-World Use Cases

This project simulates:

Business Intelligence systems
Customer analytics platforms
Data warehouse reporting systems
FinTech analytics dashboards
HR analytics systems
📊 Why This Project Matters

It demonstrates:

✔ End-to-end data engineering
✔ SQL + Python integration
✔ Real BI dashboard development
✔ Analytical thinking (OLAP)
✔ Production-style project structure

👨‍💻 Author

Shahzaib Sheikh

Data Engineer / Backend Developer
ETL & Analytics Enthusiast
Python | SQL | BI Systems
