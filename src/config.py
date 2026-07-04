from sqlalchemy import create_engine

DB_CONFIG = {
    "user": "postgres",
    "password": "123456",
    "host": "localhost",
    "port": 5432,
    "database": "user_etl_db"
}

def get_engine():
    url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    return create_engine(url)