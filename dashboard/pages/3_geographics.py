import streamlit as st

from database import run_query
from charts import bar_chart, map_chart
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

page_title("🌍 Geographic Analytics", "Location-based user intelligence")

# ==========================================================
# SECTION 1: COUNTRY DISTRIBUTION
# ==========================================================

section("🌎 Users by Country")

country_df = run_query("""
SELECT
    country,
    COUNT(*) AS total_users
FROM addresses
GROUP BY country
ORDER BY total_users DESC;
""")

fig = bar_chart(
    country_df,
    x="country",
    y="total_users",
    title="Users by Country"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 2: TOP CITIES
# ==========================================================

section("🏙 Top Cities")

city_df = run_query("""
SELECT
    city,
    COUNT(*) AS total_users
FROM addresses
GROUP BY city
ORDER BY total_users DESC
LIMIT 15;
""")

fig = bar_chart(
    city_df,
    x="city",
    y="total_users",
    title="Top Cities"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 3: GEO MAP (GLOBAL VIEW)
# ==========================================================

section("🗺 Global User Map")

map_df = run_query("""
SELECT
    u.first_name,
    u.last_name,
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
# SECTION 4: COUNTRY-CITY ANALYSIS (OLAP STYLE)
# ==========================================================

section("📊 Country-City Breakdown")

geo_df = run_query("""
SELECT
    country,
    city,
    COUNT(*) AS users
FROM addresses
GROUP BY country, city
ORDER BY users DESC
LIMIT 20;
""")

fig = bar_chart(
    geo_df,
    x="city",
    y="users",
    title="Country-City User Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 5: RAW GEO DATA
# ==========================================================

section("📄 Geographic Dataset")

df = run_query("""
SELECT
    u.id,
    u.first_name,
    a.city,
    a.country,
    a.lat,
    a.lng
FROM users u
JOIN addresses a
ON u.id = a.user_id;
""")

df = search_dataframe(df)

dataframe(df)

download_csv(df, "geo_data.csv")