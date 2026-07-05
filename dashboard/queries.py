"""
queries.py

All SQL queries used by the Streamlit Dashboard.
"""

from database import run_query


# ======================================================
# DASHBOARD KPIs
# ======================================================

def total_users():
    query = """
    SELECT COUNT(*) AS total_users
    FROM users;
    """
    return run_query(query)


def average_age():
    query = """
    SELECT ROUND(AVG(age),2) AS average_age
    FROM users;
    """
    return run_query(query)


def total_countries():
    query = """
    SELECT COUNT(DISTINCT country) AS total_countries
    FROM addresses;
    """
    return run_query(query)


def total_companies():
    query = """
    SELECT COUNT(DISTINCT name) AS total_companies
    FROM companies;
    """
    return run_query(query)


# ======================================================
# USER ANALYTICS
# ======================================================

def users_by_gender():
    query = """
    SELECT
        gender,
        COUNT(*) AS total_users
    FROM users
    GROUP BY gender
    ORDER BY total_users DESC;
    """
    return run_query(query)


def users_by_age():
    query = """
    SELECT
        age,
        COUNT(*) AS users
    FROM users
    GROUP BY age
    ORDER BY age;
    """
    return run_query(query)


def age_group_distribution():
    query = """
    SELECT

        CASE

            WHEN age < 25 THEN 'Young'

            WHEN age BETWEEN 25 AND 35 THEN 'Adult'

            WHEN age BETWEEN 36 AND 50 THEN 'Mid Age'

            ELSE 'Senior'

        END AS age_group,

        COUNT(*) AS total_users

    FROM users

    GROUP BY age_group

    ORDER BY total_users DESC;
    """

    return run_query(query)


# ======================================================
# LOCATION ANALYTICS
# ======================================================

def users_by_country():
    query = """
    SELECT

        country,

        COUNT(*) AS total_users

    FROM addresses

    GROUP BY country

    ORDER BY total_users DESC;
    """

    return run_query(query)


def top_cities():
    query = """
    SELECT

        city,

        COUNT(*) AS total_users

    FROM addresses

    GROUP BY city

    ORDER BY total_users DESC

    LIMIT 10;
    """

    return run_query(query)


def map_data():
    query = """
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
    """

    return run_query(query)


# ======================================================
# COMPANY ANALYTICS
# ======================================================

def department_distribution():
    query = """
    SELECT

        department,

        COUNT(*) AS employees

    FROM companies

    GROUP BY department

    ORDER BY employees DESC;
    """

    return run_query(query)


def company_distribution():
    query = """
    SELECT

        name,

        COUNT(*) AS employees

    FROM companies

    GROUP BY name

    ORDER BY employees DESC;
    """

    return run_query(query)


def job_titles():
    query = """
    SELECT

        title,

        COUNT(*) AS total

    FROM companies

    GROUP BY title

    ORDER BY total DESC;
    """

    return run_query(query)


# ======================================================
# BANK ANALYTICS
# ======================================================

def card_types():
    query = """
    SELECT

        card_type,

        COUNT(*) AS total_cards

    FROM bank

    GROUP BY card_type

    ORDER BY total_cards DESC;
    """

    return run_query(query)


def currencies():
    query = """
    SELECT

        currency,

        COUNT(*) AS total

    FROM bank

    GROUP BY currency

    ORDER BY total DESC;
    """

    return run_query(query)


# ======================================================
# CRYPTO ANALYTICS
# ======================================================

def crypto_distribution():
    query = """
    SELECT

        coin,

        COUNT(*) AS users

    FROM crypto

    GROUP BY coin

    ORDER BY users DESC;
    """

    return run_query(query)


def crypto_networks():
    query = """
    SELECT

        network,

        COUNT(*) AS users

    FROM crypto

    GROUP BY network

    ORDER BY users DESC;
    """

    return run_query(query)


# ======================================================
# HAIR ANALYTICS
# ======================================================

def hair_color():
    query = """
    SELECT

        color,

        COUNT(*) AS users

    FROM hair

    GROUP BY color

    ORDER BY users DESC;
    """

    return run_query(query)


def hair_type():
    query = """
    SELECT

        type,

        COUNT(*) AS users

    FROM hair

    GROUP BY type

    ORDER BY users DESC;
    """

    return run_query(query)


# ======================================================
# SCATTER PLOT
# ======================================================

def age_vs_height():
    query = """
    SELECT

        age,

        height

    FROM user_profile

    ORDER BY age;
    """

    return run_query(query)


def age_vs_weight():
    query = """
    SELECT

        age,

        weight

    FROM user_profile

    ORDER BY age;
    """

    return run_query(query)


# ======================================================
# FULL USER DETAILS
# ======================================================

def full_user_data():

    query = """

    SELECT

        u.id,

        u.first_name,
        u.last_name,

        u.age,
        u.gender,

        u.email,

        a.city,
        a.country,

        c.department,
        c.title,

        b.card_type,
        b.currency,

        cr.coin,

        d.ip

    FROM users u

    LEFT JOIN addresses a
        ON u.id = a.user_id

    LEFT JOIN companies c
        ON u.id = c.user_id

    LEFT JOIN bank b
        ON u.id = b.user_id

    LEFT JOIN crypto cr
        ON u.id = cr.user_id

    LEFT JOIN devices d
        ON u.id = d.user_id

    ORDER BY u.id;

    """

    return run_query(query)