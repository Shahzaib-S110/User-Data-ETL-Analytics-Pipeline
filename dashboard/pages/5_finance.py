import streamlit as st

from database import run_query
from charts import bar_chart, pie_chart, donut_chart
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

page_title("💳 Finance Analytics", "Banking & Crypto insights from user data")

# ==========================================================
# SECTION 1: BANK CARD TYPES
# ==========================================================

section("💳 Card Type Distribution")

card_df = run_query("""
SELECT
    card_type,
    COUNT(*) AS total_cards
FROM bank
GROUP BY card_type
ORDER BY total_cards DESC;
""")

fig = pie_chart(
    card_df,
    names="card_type",
    values="total_cards",
    title="Bank Card Types"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 2: CURRENCY DISTRIBUTION
# ==========================================================

section("💰 Currency Usage")

currency_df = run_query("""
SELECT
    currency,
    COUNT(*) AS total_users
FROM bank
GROUP BY currency
ORDER BY total_users DESC;
""")

fig = bar_chart(
    currency_df,
    x="currency",
    y="total_users",
    title="Currency Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 3: CRYPTO ANALYSIS
# ==========================================================

section("₿ Crypto Coins Usage")

crypto_df = run_query("""
SELECT
    coin,
    COUNT(*) AS users
FROM crypto
GROUP BY coin
ORDER BY users DESC;
""")

fig = donut_chart(
    crypto_df,
    names="coin",
    values="users",
    title="Crypto Coin Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 4: CRYPTO NETWORK ANALYSIS
# ==========================================================

section("🔗 Crypto Networks")

network_df = run_query("""
SELECT
    network,
    COUNT(*) AS users
FROM crypto
GROUP BY network
ORDER BY users DESC;
""")

fig = bar_chart(
    network_df,
    x="network",
    y="users",
    title="Crypto Network Usage"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 5: BANK + CRYPTO COMBINED VIEW (OLAP STYLE)
# ==========================================================

section("📊 Financial Segmentation (OLAP View)")

finance_df = run_query("""
SELECT
    b.card_type,
    b.currency,
    c.coin,
    COUNT(*) AS users
FROM bank b
JOIN crypto c
ON b.user_id = c.user_id
GROUP BY b.card_type, b.currency, c.coin
ORDER BY users DESC
LIMIT 20;
""")

fig = bar_chart(
    finance_df,
    x="card_type",
    y="users",
    title="Card Type vs Crypto Usage"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SECTION 6: RAW FINANCE DATA
# ==========================================================

section("📄 Finance Dataset")

df = run_query("""
SELECT
    b.user_id,
    b.card_type,
    b.currency,
    b.card_number,
    c.coin,
    c.network
FROM bank b
LEFT JOIN crypto c
ON b.user_id = c.user_id;
""")

df = search_dataframe(df)

dataframe(df)

download_csv(df, "finance_data.csv")