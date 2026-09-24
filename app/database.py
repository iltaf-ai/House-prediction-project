from fastapi import HTTPException
from app.config import setting

DATA_BASE_URL = setting.DATABASE

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker


engine = create_engine(
    DATA_BASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit = False
)

class Base(DeclarativeBase):
    pass


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()