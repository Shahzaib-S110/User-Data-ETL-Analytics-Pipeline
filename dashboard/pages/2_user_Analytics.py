import streamlit as st

from database import run_query
from queries import (
    users_by_gender,
    age_group_distribution
)

from charts import (
    bar_chart,
    histogram,
    scatter_chart,
    pie_chart
)

from utils import (
    page_title,
    section,
    search_dataframe,
    dataframe,
    download_csv,
    gender_filter,
    age_filter
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

page_title("👤 User Analytics", "Deep statistical analysis of users")

# ==========================================================
# LOAD BASE DATA
# ==========================================================

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
    c.title,
    b.card_type,
    cr.coin
FROM users u
LEFT JOIN addresses a ON u.id = a.user_id
LEFT JOIN companies c ON u.id = c.user_id
LEFT JOIN bank b ON u.id = b.user_id
LEFT JOIN crypto cr ON u.id = cr.user_id;
""")

# ==========================================================
# FILTERS (SIDEBAR STYLE)
# ==========================================================

df = gender_filter(df)
df = age_filter(df)

# ==========================================================
# SECTION 1: AGE DISTRIBUTION
# ==========================================================

section("🎂 Age Distribution")

fig = histogram(
    df,
    column="age",
    title="User Age Distribution",
    bins=10
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 2: AGE GROUPS (OLAP STYLE)
# ==========================================================

section("📊 Age Group Analysis")

age_group_df = age_group_distribution()

fig = bar_chart(
    age_group_df,
    x="age_group",
    y="total_users",
    title="Age Group Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 3: GENDER DISTRIBUTION
# ==========================================================

section("🚻 Gender Analysis")

gender_df = users_by_gender()

fig = pie_chart(
    gender_df,
    names="gender",
    values="total_users",
    title="Gender Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 4: CITY + COUNTRY BREAKDOWN
# ==========================================================

section("🌍 Location Insights")

location_df = run_query("""
SELECT
    a.city,
    a.country,
    COUNT(*) AS users
FROM addresses a
GROUP BY a.city, a.country
ORDER BY users DESC
LIMIT 15;
""")

fig = bar_chart(
    location_df,
    x="city",
    y="users",
    title="Top Cities by Users"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 7: RAW DATA TABLE
# ==========================================================

section("📄 Filtered User Data")

df = search_dataframe(df)

dataframe(df)

download_csv(df, "user_analytics.csv")