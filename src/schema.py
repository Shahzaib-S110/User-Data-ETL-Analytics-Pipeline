from config import get_engine
from sqlalchemy import text

def create_tables():
    engine = get_engine()

    with engine.begin() as conn:

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender TEXT,
            email TEXT,
            phone TEXT,
            username TEXT,
            birth_date DATE
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS addresses (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            city TEXT,
            state TEXT,
            postal_code TEXT,
            country TEXT,
            lat DOUBLE PRECISION,
            lng DOUBLE PRECISION
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS hair (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            color TEXT,
            type TEXT
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS bank (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            card_number TEXT,
            card_type TEXT,
            currency TEXT,
            iban TEXT
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            name TEXT,
            department TEXT,
            title TEXT
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS company_addresses (
            id SERIAL PRIMARY KEY,
            company_id INTEGER REFERENCES companies(id),
            city TEXT,
            state TEXT,
            country TEXT,
            lat DOUBLE PRECISION,
            lng DOUBLE PRECISION
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS crypto (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            coin TEXT,
            wallet TEXT,
            network TEXT
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS devices (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            ip TEXT,
            mac_address TEXT,
            user_agent TEXT
        );
        """))