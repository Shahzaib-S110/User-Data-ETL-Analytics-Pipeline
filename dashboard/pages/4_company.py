import streamlit as st

from database import run_query
from charts import bar_chart, donut_chart, pie_chart
from utils import (
    page_title,
    section,
    search_dataframe,
    dataframe,
    download_csv
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

page_title("💼 Company Analytics", "HR & organizational insights from user data")

# ==========================================================
# SECTION 1: DEPARTMENT ANALYSIS
# ==========================================================

section("🏢 Departments Overview")

dept_df = run_query("""
SELECT
    department,
    COUNT(*) AS total_employees
FROM companies
GROUP BY department
ORDER BY total_employees DESC;
""")

fig = donut_chart(
    dept_df,
    names="department",
    values="total_employees",
    title="Department Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 2: JOB TITLES ANALYSIS
# ==========================================================

section("👔 Job Titles")

title_df = run_query("""
SELECT
    title,
    COUNT(*) AS total_employees
FROM companies
GROUP BY title
ORDER BY total_employees DESC
LIMIT 15;
""")

fig = bar_chart(
    title_df,
    x="title",
    y="total_employees",
    title="Top Job Titles"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 3: COMPANY DISTRIBUTION
# ==========================================================

section("🏭 Company Distribution")

company_df = run_query("""
SELECT
    name AS company,
    COUNT(*) AS employees
FROM companies
GROUP BY name
ORDER BY employees DESC
LIMIT 15;
""")

fig = bar_chart(
    company_df,
    x="company",
    y="employees",
    title="Top Companies"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 4: DEPARTMENT vs TITLE (OLAP STYLE)
# ==========================================================

section("📊 Department vs Job Role Analysis")

olap_df = run_query("""
SELECT
    department,
    title,
    COUNT(*) AS employees
FROM companies
GROUP BY department, title
ORDER BY employees DESC
LIMIT 20;
""")

fig = bar_chart(
    olap_df,
    x="title",
    y="employees",
    title="Department vs Job Title"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 5: FULL COMPANY DATA
# ==========================================================

section("📄 Company Dataset")

df = run_query("""
SELECT
    c.user_id,
    c.name,
    c.department,
    c.title,
    a.city,
    a.country
FROM companies c
LEFT JOIN addresses a
ON c.user_id = a.user_id;
""")

df = search_dataframe(df)

dataframe(df)

download_csv(df, "company_data.csv")