import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:123456@localhost:5432/user_etl_db"
)

df = pd.read_sql("SELECT * FROM users", engine)


st.title("User Analytics Dashboard")

st.metric("Total Users", len(df))
st.metric("Average Age", round(df["age"].mean(), 1))
st.metric("Male Users", len(df[df["gender"] == "male"]))
st.metric("Female Users", len(df[df["gender"] == "female"]))

# Gender Chart
import plotly.express as px

gender = df["gender"].value_counts().reset_index()
gender.columns = ["Gender", "Users"]

fig = px.bar(
    gender,
    x="Gender",
    y="Users",
    title="Users by Gender"
)

st.plotly_chart(fig, use_container_width=True)


# Age Distribution
fig = px.histogram(
    df,
    x="age",
    nbins=10,
    title="Age Distribution"
)

st.plotly_chart(fig, use_container_width=True)