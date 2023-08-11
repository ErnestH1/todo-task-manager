from fastapi import FastAPI
from database import engine
from model import Base
from task import app as task_app
from auth import app as auth_app

app = FastAPI()

# Include the task and auth routers with specified prefixes and tags
app.include_router(auth_app, prefix="/auth", tags=["Authentication"])
app.include_router(task_app, prefix="/task", tags=["Task"])

# Create the database tables
Base.metadata.create_all(bind=engine)
