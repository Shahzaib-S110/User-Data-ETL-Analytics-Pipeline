import streamlit as st

from database import run_query
from queries import (
    users_by_gender,
    users_by_country,
    top_cities,
    department_distribution,
    card_types,
    crypto_distribution,
    total_users,
    average_age
)

from charts import (
    bar_chart,
    pie_chart,
    donut_chart,
    map_chart
)

from utils import (
    page_title,
    kpi_row,
    section,
    search_dataframe,
    dataframe,
    download_csv
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

page_title("🏠 Home Dashboard", "Executive Overview of User ETL Analytics")

# ==========================================================
# KPI METRICS
# ==========================================================

total_users_value = total_users()["total_users"][0]
avg_age_value = average_age()["average_age"][0]

countries_value = run_query("""
SELECT COUNT(DISTINCT country) AS c FROM addresses;
""")["c"][0]

companies_value = run_query("""
SELECT COUNT(DISTINCT name) AS c FROM companies;
""")["c"][0]

kpi_row(
    total_users_value,
    avg_age_value,
    countries_value,
    companies_value
)

st.divider()

# ==========================================================
# SECTION 1: USER DISTRIBUTION
# ==========================================================

section("👤 User Distribution")

col1, col2 = st.columns(2)

with col1:

    gender_df = users_by_gender()

    fig = pie_chart(
        gender_df,
        names="gender",
        values="total_users",
        title="Gender Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    country_df = users_by_country()

    fig = bar_chart(
        country_df.head(10),
        x="country",
        y="total_users",
        title="Top Countries"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 2: CITY ANALYSIS
# ==========================================================

section("🏙 Top Cities")

city_df = top_cities()

fig = bar_chart(
    city_df,
    x="city",
    y="total_users",
    title="Top 10 Cities"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 3: COMPANY ANALYSIS
# ==========================================================

section("💼 Company Insights")

col1, col2 = st.columns(2)

with col1:

    dept_df = department_distribution()

    fig = donut_chart(
        dept_df,
        names="department",
        values="employees",
        title="Departments"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    card_df = card_types()

    fig = pie_chart(
        card_df,
        names="card_type",
        values="total_cards",
        title="Bank Card Types"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 4: CRYPTO ANALYSIS
# ==========================================================

section("₿ Crypto Usage")

crypto_df = crypto_distribution()

fig = bar_chart(
    crypto_df,
    x="coin",
    y="users",
    title="Crypto Coin Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 5: MAP VISUALIZATION
# ==========================================================

section("🌍 Global User Map")

map_df = run_query("""
SELECT
    u.first_name,
    a.city,
    a.country,
    a.lat,
    a.lng
FROM users u
JOIN addresses a
ON u.id = a.user_id;
""")

fig = map_chart(map_df)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 6: RAW DATA PREVIEW
# ==========================================================

section("📄 Sample Data Preview")

df = run_query("""
SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.age,
    u.gender,
    a.city,
    a.country,
    c.department,
    b.card_type
FROM users u
LEFT JOIN addresses a ON u.id = a.user_id
LEFT JOIN companies c ON u.id = c.user_id
LEFT JOIN bank b ON u.id = b.user_id
LIMIT 20;
""")

df = search_dataframe(df)

dataframe(df)

download_csv(df, "home_data.csv")