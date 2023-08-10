# main.py

from fastapi import FastAPI
from database import engine
from model import Base

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)
