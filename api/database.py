# database/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
