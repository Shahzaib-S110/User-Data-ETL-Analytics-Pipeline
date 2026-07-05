# 📊 User Data ETL & Analytics Pipeline (PostgreSQL + Streamlit)

A complete **end-to-end Data Engineering + Analytics project** that extracts user data from an API, transforms it using Python, loads it into PostgreSQL, and visualizes insights through an interactive Streamlit dashboard.

This project demonstrates a real-world **ETL pipeline + OLAP analytics system + BI dashboard**.

---

## 🚀 Overview

This system performs a full data workflow:

- 🔄 Extract data from DummyJSON API
- 🧹 Transform & clean using Pandas
- 🗄️ Load structured data into PostgreSQL
- 📊 Run SQL-based analytical queries (OLAP)
- 📈 Visualize insights using Streamlit + Plotly

---

## 🏗️ Architecture


DummyJSON API
↓
[ Extract Layer - Python Requests ]
↓
[ Transform Layer - Pandas ]
↓
[ Load Layer - PostgreSQL ]
↓
[ SQL Analytics - OLAP Queries ]
↓
[ Streamlit Dashboard - BI Layer ]


---

## ⚙️ Tech Stack

- 🐍 Python 3.10+
- 🗄️ PostgreSQL
- 🧮 Pandas
- 🔗 SQLAlchemy
- 📊 Streamlit
- 📈 Plotly
- 📉 Seaborn (EDA)

---

## 📁 Project Structure


User-Data-ETL-Analytics-Pipeline/
│
├── src/ # ETL Pipeline
│ ├── extract.py # Fetch data from API
│ ├── transform.py # Data cleaning & feature engineering
│ ├── load.py # Load data into PostgreSQL
│ ├── schema.py # Database schema definition
│ ├── database.py # DB connection handler
│ └── main.py # ETL pipeline entry point
│
├── dashboard/ # Streamlit Dashboard
│ ├── app.py # Main Streamlit app
│ ├── database.py # DB connection for dashboard
│ ├── queries.py # SQL analytics queries
│ ├── charts.py # Plotly visualizations
│ ├── utils.py # Helper functions
│ └── pages/ # Multi-page dashboard views
│
├── sql/ # SQL scripts (optional)
│ ├── create_tables.sql
│ ├── analytics_queries.sql
│
├── data/ # Raw / processed data (optional)
│
├── requirements.txt
└── README.md


---

## 🔄 ETL Pipeline

### 1️⃣ Extract Layer
- Fetch user data from **DummyJSON API**
- Handle pagination & API response errors
- Store raw JSON (optional for debugging)

### 2️⃣ Transform Layer
- Clean missing/null values
- Normalize nested JSON structures
- Feature engineering:
  - Age groups (18–25, 26–35, etc.)
  - BMI calculation
  - Email domain extraction
  - Address flattening

### 3️⃣ Load Layer
- Load structured data into PostgreSQL tables:

**Tables:**
- `users`
- `addresses`
- `companies`
- `bank`
- `crypto`
- `devices`
- `hair`

---

## 🗄️ Database Schema (Overview)


users (id, name, gender, age, email, phone)
addresses (id, user_id, city, country)
companies (id, user_id, company_name)
bank (id, user_id, card_type, currency)
crypto (id, user_id, coin, wallet)
devices (id, user_id, device_type)
hair (id, user_id, color, type)


---

## 📊 Analytics (SQL / OLAP)

This project supports advanced analytical queries:

### 🔹 Aggregations
```sql
SELECT gender, COUNT(*) AS total_users
FROM users
GROUP BY gender;
🔹 Age Segmentation
SELECT
  CASE
    WHEN age BETWEEN 18 AND 25 THEN '18-25'
    WHEN age BETWEEN 26 AND 35 THEN '26-35'
    ELSE '36+'
  END AS age_group,
  COUNT(*)
FROM users
GROUP BY age_group;
🔹 JOIN Analysis
SELECT u.name, a.city, c.company_name
FROM users u
JOIN addresses a ON u.id = a.user_id
JOIN companies c ON u.id = c.user_id;
🔹 Ranking
SELECT name, age,
RANK() OVER (ORDER BY age DESC) AS age_rank
FROM users;
📈 Dashboard Features (Streamlit)
📊 User distribution charts
🌍 Country-wise analysis
👥 Gender distribution
🏢 Company insights
📱 Device usage analysis
📈 Age segmentation visuals
🔎 Filter-based interactive analytics
▶️ How to Run the Project
1. Clone Repository
git clone https://github.com/your-username/User-Data-ETL-Analytics-Pipeline.git
cd User-Data-ETL-Analytics-Pipeline
2. Install Dependencies
pip install -r requirements.txt
3. Setup PostgreSQL

Create database:

CREATE DATABASE user_etl_db;
4. Run ETL Pipeline
python src/main.py
5. Run Dashboard
streamlit run dashboard/app.py
📦 Requirements
pandas
requests
sqlalchemy
psycopg2
streamlit
plotly
seaborn
📌 Key Learnings
Real-world ETL pipeline design
API data ingestion
Relational database modeling
SQL OLAP analytics
Data visualization dashboards
End-to-end data engineering workflow
🚀 Future Improvements
Airflow orchestration ⏱️
Docker containerization 🐳
CI/CD pipeline (GitHub Actions)
AWS deployment (RDS + EC2)
Real-time streaming (Kafka)
Role-based dashboard authentication
👨‍💻 Author

Shahzaib Sheikh
Data Engineering & AI Enthusiast
