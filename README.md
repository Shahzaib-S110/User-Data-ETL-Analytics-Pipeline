# 📊 User Data ETL & Analytics Pipeline

A complete end-to-end **Data Engineering & Analytics** project that extracts user data from the **DummyJSON API**, transforms and cleans it using **Python**, loads it into **PostgreSQL**, and presents business insights through an interactive **Streamlit** dashboard.

This project demonstrates a production-style **ETL pipeline**, **relational database design**, **SQL-based OLAP analytics**, and **interactive business intelligence visualization**.

---
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/22da83c6-906d-40ec-a2d1-105ebfa331ca" />


# 🚀 Project Overview

The pipeline automates the complete data engineering workflow:

- 🔄 Extract user data from the DummyJSON API
- 🧹 Clean and transform raw data using Pandas
- 🗄️ Load structured data into PostgreSQL
- 📊 Perform SQL-based analytical (OLAP) queries
- 📈 Visualize insights with Streamlit and Plotly

---

# 🏗️ System Architecture

```text
             DummyJSON API
                   │
                   ▼
       Extract Layer (Python Requests)
                   │
                   ▼
      Transform Layer (Pandas Cleaning)
                   │
                   ▼
       Load Layer (PostgreSQL Database)
                   │
                   ▼
        SQL Analytics (OLAP Queries)
                   │
                   ▼
      Streamlit Dashboard (BI Layer)
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3.10+ | ETL Development |
| 🗄️ PostgreSQL | Relational Database |
| 🧮 Pandas | Data Cleaning & Transformation |
| 🔗 SQLAlchemy | Database ORM |
| 🐘 psycopg2 | PostgreSQL Connector |
| 📊 Streamlit | Interactive Dashboard |
| 📈 Plotly | Interactive Charts |
| 📉 Seaborn | Statistical Visualization |

---

# 📁 Project Structure

```text
User-Data-ETL-Analytics-Pipeline/
│
├── dashboard/
│   ├── app.py
│   ├── database.py
│   ├── queries.py
│   ├── charts.py
│   ├── utils.py
│   │
│   └── pages/
│       ├── 1_Home.py
│       ├── 2_User_Analytics.py
│       ├── 3_Geographics.py
│       ├── 4_Company.py
│       ├── 5_Finance.py
│       └── 6_Raw_Data.py
│
├── src/
│   ├── data/
│   │    │__raw/
│   │    │__user.json
│   │
│   ├── plots/
│   │
│   ├── config.py
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analysis.py
│   └── database.py
│
├── sql/
│
├── requirements.txt
└── README.md
```

---

# 🔄 ETL Pipeline

## 1️⃣ Extract

- Retrieve user data from the DummyJSON API
- Handle API pagination
- Handle request failures and exceptions
- Optionally store raw JSON for debugging

---

## 2️⃣ Transform

Data preprocessing includes:

- Removing missing values
- Normalizing nested JSON objects
- Flattening address information
- Standardizing column names
- Feature engineering

### Engineered Features

- Age Groups
- Email Domain
- BMI Calculation
- Flattened Address Information

---

## 3️⃣ Load

Load cleaned data into normalized PostgreSQL tables.

### Database Tables

- **users**
- **addresses**
- **companies**
- **bank**
- **crypto**
- **devices**
- **hair**

---

# 🗄️ Database Schema

## users

| Column | Type |
|---------|------|
| id | Integer |
| name | Text |
| gender | Text |
| age | Integer |
| email | Text |
| phone | Text |

---

## addresses

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| city | Text |
| country | Text |

---

## companies

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| company_name | Text |

---

## bank

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| card_type | Text |
| currency | Text |

---

## crypto

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| coin | Text |
| wallet | Text |

---

## devices

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| device_type | Text |

---

## hair

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| color | Text |
| type | Text |

---

# 📊 SQL Analytics

## Gender Distribution

```sql
SELECT gender,
       COUNT(*) AS total_users
FROM users
GROUP BY gender;
```

---

## Age Segmentation

```sql
SELECT
CASE
    WHEN age BETWEEN 18 AND 25 THEN '18-25'
    WHEN age BETWEEN 26 AND 35 THEN '26-35'
    ELSE '36+'
END AS age_group,
COUNT(*) AS total_users
FROM users
GROUP BY age_group;
```

---

## User, Company & Address Analysis

```sql
SELECT
u.name,
a.city,
c.company_name
FROM users u
JOIN addresses a
ON u.id = a.user_id
JOIN companies c
ON u.id = c.user_id;
```

---

## Age Ranking

```sql
SELECT
name,
age,
RANK() OVER (ORDER BY age DESC) AS age_rank
FROM users;
```

---

# 📈 Dashboard Features

The Streamlit dashboard provides interactive business insights including:

- 📊 User Distribution
- 👥 Gender Analysis
- 🌍 Country-wise Distribution
- 🏢 Company Insights
- 📱 Device Usage Analysis
- 📈 Age Group Visualization
- 🔎 Interactive Filters
- 📉 Dynamic Plotly Charts

---

# ▶️ Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/User-Data-ETL-Analytics-Pipeline.git

cd User-Data-ETL-Analytics-Pipeline
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Create PostgreSQL Database

```sql
CREATE DATABASE user_etl_db;
```

---

## 4. Configure Database

Update your PostgreSQL credentials inside:

```text
src/database.py
dashboard/database.py
```

---

## 5. Run the ETL Pipeline

```bash
python src/main.py
```

---

## 6. Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📦 Requirements

```text
pandas
requests
sqlalchemy
psycopg2
streamlit
plotly
seaborn
```

Install using:

```bash
pip install -r requirements.txt
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- End-to-End ETL Pipeline Development
- REST API Data Ingestion
- Data Cleaning & Transformation
- PostgreSQL Database Modeling
- SQL OLAP Analytics
- Window Functions & Joins
- Interactive BI Dashboard Development
- Data Visualization with Plotly
- Python Data Engineering Best Practices

---

# 🚀 Future Improvements

Planned enhancements include:

- ⏱️ Apache Airflow Orchestration
- 🐳 Docker Containerization
- ☁️ AWS Deployment (EC2 + RDS)
- ⚡ Kafka Streaming Pipeline
- 🔐 Role-Based Authentication
- 📅 ETL Scheduling with Cron Jobs
- 🔄 Incremental Data Loading
- 🚀 GitHub Actions CI/CD Pipeline

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Shahzaib Sheikh**

**Data Engineering | AI | Machine Learning Enthusiast**

If you found this project helpful, consider giving it a ⭐ on GitHub.
