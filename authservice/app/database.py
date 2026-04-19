from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres:5432/ecommerce")

# Ensure SSL is required for the connection
if "sslmode" not in DATABASE_URL:
    DATABASE_URL += ("&" if "?" in DATABASE_URL else "?") + "sslmode=require"

engine = None

# Retry DB connection
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        print("✅ Connected to PostgreSQL")
        break
    except Exception as e:
        print(f"⏳ DB not ready... retrying {i+1}/10")
        time.sleep(3)

if engine is None:
    raise Exception("❌ Could not connect to DB")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()