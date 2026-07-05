import streamlit as st

from database import run_query, get_tables, load_table
from utils import (
    page_title,
    section,
    search_dataframe,
    dataframe,
    download_csv,
    warning
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

page_title("📄 Raw Data Explorer", "Inspect all PostgreSQL tables & run queries")

# ==========================================================
# SECTION 1: TABLE SELECTOR
# ==========================================================

section("🗄 Database Tables")

tables_df = get_tables()

table_list = tables_df["table_name"].tolist()

selected_table = st.selectbox(
    "Select a table",
    table_list
)

df = load_table(selected_table)

st.success(f"Loaded table: {selected_table}")

# ==========================================================
# SECTION 2: SEARCH INSIDE TABLE
# ==========================================================

section("🔍 Search Data")

df = search_dataframe(df)

# ==========================================================
# SECTION 3: DATA PREVIEW
# ==========================================================

section("📊 Table Preview")

dataframe(df)

# ==========================================================
# SECTION 4: DOWNLOAD
# ==========================================================

download_csv(df, f"{selected_table}.csv")

# ==========================================================
# SECTION 5: BASIC STATISTICS
# ==========================================================

section("📈 Quick Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", len(df))

with col2:
    st.metric("Columns", len(df.columns))

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())

# ==========================================================
# SECTION 6: CUSTOM SQL QUERY RUNNER
# ==========================================================

section("⚙ SQL Query Runner")

st.markdown("Write a SQL query below:")

query = st.text_area(
    "SQL Query",
    height=150,
    placeholder="SELECT * FROM users LIMIT 10;"
)

if st.button("Run Query"):

    try:

        result = run_query(query)

        st.success("Query executed successfully!")

        dataframe(result)

        download_csv(result, "query_result.csv")

    except Exception as e:

        st.error(f"Query Error: {e}")

# ==========================================================
# SECTION 7: DATA QUALITY CHECK
# ==========================================================

section("🧹 Data Quality Check")

st.markdown("Checking NULL values per column:")

null_counts = df.isnull().sum().reset_index()

null_counts.columns = ["column", "null_values"]

dataframe(null_counts)

# ==========================================================
# SECTION 8: FULL TABLE INSIGHT
# ==========================================================

with st.expander("📊 Full Table Summary"):

    st.write(df.describe(include="all"))

# ==========================================================
# WARNING SECTION
# ==========================================================

warning("""
This is a RAW data layer.

Use carefully for debugging, analysis, or ETL validation.
""")