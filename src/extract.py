import requests
import json
import os

URL = "https://dummyjson.com/users"

def fetch_users():
    res = requests.get(URL)
    return res.json()["users"]

def save_raw(users):
    os.makedirs("data/raw", exist_ok=True)

    with open("data/raw/users.json", "w") as f:
        json.dump(users, f, indent=4)

def run_extract():
    users = fetch_users()
    save_raw(users)
    print(f"Extracted {len(users)} users")