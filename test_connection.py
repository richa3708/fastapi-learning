from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("✅ Connected to PostgreSQL successfully!")
except Exception as e:
    print("❌ Connection failed!")
    print(e)