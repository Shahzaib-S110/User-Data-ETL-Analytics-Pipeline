import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# ==============================
# PostgreSQL Connection Settings
# ==============================

DB_CONFIG = {
    "user": "postgres",
    "password": "123456",
    "host": "localhost",
    "port": 5432,
    "database": "user_etl_db"
}


# ==============================
# Create SQLAlchemy Engine
# ==============================

@st.cache_resource
def get_engine():
    """
    Create a SQLAlchemy engine.
    Streamlit caches this so the connection
    is created only once.
    """

    connection_string = (
        f"postgresql+psycopg2://"
        f"{DB_CONFIG['user']}:"
        f"{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )

    engine = create_engine(connection_string)

    return engine


# ==============================
# Execute SQL Query
# ==============================

@st.cache_data
def run_query(query):
    """
    Execute any SQL query
    and return a Pandas DataFrame.
    """

    engine = get_engine()

    with engine.connect() as connection:
        df = pd.read_sql(text(query), connection)

    return df


# ==============================
# Execute SQL Command
# (INSERT / UPDATE / DELETE)
# ==============================

def execute_query(query):
    """
    Execute SQL statements
    that don't return rows.
    """

    engine = get_engine()

    with engine.begin() as connection:
        connection.execute(text(query))


# ==============================
# Get Table Names
# ==============================

@st.cache_data
def get_tables():
    """
    Return all public tables
    from PostgreSQL.
    """

    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    ORDER BY table_name;
    """

    return run_query(query)


# ==============================
# Get Row Count
# ==============================

@st.cache_data
def get_row_count(table_name):
    """
    Return number of rows
    in a table.
    """

    query = f"""
    SELECT COUNT(*) AS total_rows
    FROM {table_name};
    """

    return run_query(query).iloc[0]["total_rows"]


# ==============================
# Database Health Check
# ==============================

def test_connection():
    """
    Test whether PostgreSQL
    is reachable.
    """

    try:

        engine = get_engine()

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return True

    except Exception as e:

        st.error(e)

        return False


# ==============================
# Load Entire Table
# ==============================

@st.cache_data
def load_table(table_name):
    """
    Load a complete table
    into a DataFrame.
    """

    query = f"""
    SELECT *
    FROM {table_name};
    """

    return run_query(query)


# ==============================
# Dashboard Statistics
# ==============================

@st.cache_data
def get_dashboard_stats():
    """
    Returns basic dashboard KPIs.
    """

    query = """
    SELECT

        COUNT(*) AS total_users,

        ROUND(AVG(age),2) AS average_age,

        COUNT(DISTINCT gender) AS genders,

        COUNT(DISTINCT username) AS usernames

    FROM users;
    """

    return run_query(query)