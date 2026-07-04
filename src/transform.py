import json
import pandas as pd

def load_raw():
    with open("data/raw/users.json", "r") as f:
        return json.load(f)


def transform(users):

    users_table = []
    addresses = []
    hair = []
    bank = []
    companies = []
    company_addresses = []
    crypto = []
    devices = []

    for u in users:

        users_table.append({
            "id": u["id"],
            "first_name": u["firstName"],
            "last_name": u["lastName"],
            "age": u["age"],
            "gender": u["gender"],
            "email": u["email"],
            "phone": u["phone"],
            "username": u["username"],
            "birth_date": u["birthDate"]
        })

        addresses.append({
            "user_id": u["id"],
            "city": u["address"]["city"],
            "state": u["address"]["state"],
            "postal_code": u["address"]["postalCode"],
            "country": u["address"]["country"],
            "lat": u["address"]["coordinates"]["lat"],
            "lng": u["address"]["coordinates"]["lng"]
        })

        hair.append({
            "user_id": u["id"],
            "color": u["hair"]["color"],
            "type": u["hair"]["type"]
        })

        bank.append({
            "user_id": u["id"],
            "card_number": u["bank"]["cardNumber"],
            "card_type": u["bank"]["cardType"],
            "currency": u["bank"]["currency"],
            "iban": u["bank"]["iban"]
        })

        companies.append({
            "user_id": u["id"],
            "name": u["company"]["name"],
            "department": u["company"]["department"],
            "title": u["company"]["title"]
        })

        company_addresses.append({
            "company_id": u["id"],   # simplified mapping
            "city": u["company"]["address"]["city"],
            "state": u["company"]["address"]["state"],
            "country": u["company"]["address"]["country"],
            "lat": u["company"]["address"]["coordinates"]["lat"],
            "lng": u["company"]["address"]["coordinates"]["lng"]
        })

        crypto.append({
            "user_id": u["id"],
            "coin": u["crypto"]["coin"],
            "wallet": u["crypto"]["wallet"],
            "network": u["crypto"]["network"]
        })

        devices.append({
            "user_id": u["id"],
            "ip": u["ip"],
            "mac_address": u["macAddress"],
            "user_agent": u["userAgent"]
        })

    return (
        pd.DataFrame(users_table),
        pd.DataFrame(addresses),
        pd.DataFrame(hair),
        pd.DataFrame(bank),
        pd.DataFrame(companies),
        pd.DataFrame(company_addresses),
        pd.DataFrame(crypto),
        pd.DataFrame(devices),
    )

print("Data Transformation Completed ✅")   