import pandas as pd
from config import get_engine
import os
import matplotlib.pyplot as plt



engine = get_engine()

query = """
SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.age,
    u.gender,
    u.email,
    u.username,
    a.city,
    a.state,
    a.country,
    h.color AS hair_color,
    h.type AS hair_type,
    b.currency,
    c.name AS company_name,
    c.department,
    c.title,
    cr.coin,
    cr.network
FROM users u
LEFT JOIN addresses a
    ON u.id = a.user_id
LEFT JOIN hair h
    ON u.id = h.user_id
LEFT JOIN bank b
    ON u.id = b.user_id
LEFT JOIN companies c
    ON u.id = c.user_id
LEFT JOIN crypto cr
    ON u.id = cr.user_id;
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.info())


df["gender"] = df["gender"].str.lower().str.strip()

df["city"] = df["city"].str.title().str.strip()

df["country"] = df["country"].str.title().str.strip()

df.drop_duplicates(inplace=True)

print(df.groupby("gender")["age"].mean())

print(df["country"].value_counts())

print(df["city"].value_counts().head(10))

print(df["coin"].value_counts())

os.makedirs("plots", exist_ok=True)


# Visualization 1 — Users by Gender
plt.figure(figsize=(6,4))

gender_counts = df["gender"].value_counts()

gender_counts.plot(kind="bar")

plt.title("Users by Gender")

plt.xlabel("Gender")

plt.ylabel("Number of Users")

plt.tight_layout()

plt.savefig("plots/users_by_gender.png")

plt.close()

# Visualization 2 — Average Age by Gender
avg_age = df.groupby("gender")["age"].mean()

plt.figure(figsize=(6,4))

avg_age.plot(kind="bar")

plt.title("Average Age by Gender")

plt.xlabel("Gender")

plt.ylabel("Average Age")

plt.tight_layout()

plt.savefig("plots/average_age_by_gender.png")

plt.close()

# Visualization 3 — Top Cities
top_cities = df["city"].value_counts().head(10)

plt.figure(figsize=(8,5))

top_cities.plot(kind="bar")

plt.title("Top Cities")

plt.xlabel("City")

plt.ylabel("Number of Users")

plt.tight_layout()

plt.savefig("plots/top_cities.png")

plt.close()

# Visualization 4 — Hair Color Distribution
plt.figure(figsize=(6,4))

hair_color_counts = df["hair_color"].value_counts()

hair_color_counts.plot(kind="bar")

plt.title("Hair Color Distribution")

plt.xlabel("Hair Color")

plt.ylabel("Number of Users")

plt.tight_layout()

plt.savefig("plots/hair_color_distribution.png")

plt.close()


# Visualization 5 — Cryptocurrency Usage
plt.figure(figsize=(6,4))

coin_counts = df["coin"].value_counts()

coin_counts.plot(kind="bar")

plt.title("Cryptocurrency Usage")

plt.xlabel("Cryptocurrency")

plt.ylabel("Number of Users")

plt.tight_layout()

plt.savefig("plots/cryptocurrency_usage.png")

plt.close()

print("Data Analysis and Visualization Completed ✅")