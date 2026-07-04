from schema import create_tables
from extract import run_extract
from transform import load_raw, transform
from load import load_df

def run_pipeline():

    create_tables()
    run_extract()

    users = load_raw()

    (
        users_df,
        addr_df,
        hair_df,
        bank_df,
        company_df,
        company_addr_df,
        crypto_df,
        device_df
    ) = transform(users)

    load_df(users_df, "users")
    load_df(addr_df, "addresses")
    load_df(hair_df, "hair")
    load_df(bank_df, "bank")
    load_df(company_df, "companies")
    load_df(company_addr_df, "company_addresses")
    load_df(crypto_df, "crypto")
    load_df(device_df, "devices")

    print("ETL Pipeline Completed 🚀")

if __name__ == "__main__":
    run_pipeline()