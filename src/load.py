from config import get_engine

def load_df(df, table_name):
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists="append", index=False)