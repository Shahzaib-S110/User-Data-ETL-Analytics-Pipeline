import streamlit as st
import pandas as pd


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

def configure_page():

    st.set_page_config(
        page_title="User Analytics Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )


# ==========================================================
# CUSTOM CSS
# ==========================================================

def load_css():

    st.markdown(
        """
        <style>

        .main{
            padding-top:20px;
        }

        div[data-testid="metric-container"]{

            background:#f8f9fa;

            border-radius:12px;

            padding:15px;

            box-shadow:0px 2px 8px rgba(0,0,0,0.1);

        }

        footer{
            visibility:hidden;
        }

        header{
            visibility:hidden;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# PAGE TITLE
# ==========================================================

def page_title(title, subtitle=None):

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()


# ==========================================================
# SIDEBAR
# ==========================================================

def sidebar():

    st.sidebar.title("📊 Dashboard")

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
        **User ETL Analytics**

        DummyJSON API

        PostgreSQL

        Streamlit

        Plotly
        """
    )

    st.sidebar.markdown("---")


# ==========================================================
# KPI ROW
# ==========================================================

def kpi_row(
    total_users,
    avg_age,
    countries,
    companies
):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "👤 Total Users",
            total_users
        )

    with c2:
        st.metric(
            "🎂 Average Age",
            avg_age
        )

    with c3:
        st.metric(
            "🌍 Countries",
            countries
        )

    with c4:
        st.metric(
            "🏢 Companies",
            companies
        )


# ==========================================================
# SEARCH
# ==========================================================

def search_dataframe(df):

    keyword = st.text_input(
        "🔍 Search"
    )

    if keyword:

        keyword = keyword.lower()

        mask = df.astype(str).apply(
            lambda col:
            col.str.lower().str.contains(keyword)
        ).any(axis=1)

        df = df[mask]

    return df


# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

def download_csv(df, filename):

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name=filename,
        mime="text/csv"
    )


# ==========================================================
# SHOW DATAFRAME
# ==========================================================

def dataframe(df):

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# SECTION HEADER
# ==========================================================

def section(title):

    st.subheader(title)

    st.markdown("---")


# ==========================================================
# FILTER BY GENDER
# ==========================================================

def gender_filter(df):

    genders = sorted(df["gender"].dropna().unique())

    selected = st.sidebar.multiselect(
        "Gender",
        genders,
        default=genders
    )

    return df[
        df["gender"].isin(selected)
    ]


# ==========================================================
# FILTER BY COUNTRY
# ==========================================================

def country_filter(df):

    if "country" not in df.columns:
        return df

    countries = sorted(
        df["country"].dropna().unique()
    )

    selected = st.sidebar.multiselect(
        "Country",
        countries,
        default=countries
    )

    return df[
        df["country"].isin(selected)
    ]


# ==========================================================
# FILTER AGE
# ==========================================================

def age_filter(df):

    if "age" not in df.columns:
        return df

    minimum = int(df["age"].min())
    maximum = int(df["age"].max())

    age = st.sidebar.slider(
        "Age",
        minimum,
        maximum,
        (minimum, maximum)
    )

    return df[
        (df["age"] >= age[0]) &
        (df["age"] <= age[1])
    ]


# ==========================================================
# SUCCESS MESSAGE
# ==========================================================

def success(msg):

    st.success(msg)


# ==========================================================
# ERROR MESSAGE
# ==========================================================

def error(msg):

    st.error(msg)


# ==========================================================
# WARNING MESSAGE
# ==========================================================

def warning(msg):

    st.warning(msg)


# ==========================================================
# INFO BOX
# ==========================================================

def info(msg):

    st.info(msg)


# ==========================================================
# FOOTER
# ==========================================================

def footer():

    st.markdown("---")

    st.caption(
        "Built with ❤️ using Python, PostgreSQL, SQLAlchemy, Plotly & Streamlit"
    )