from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from auth import get_current_user
from model import Task, CompletedTask,User

app = APIRouter()

# Create task
@app.post("/tasks/")
def create_task(description: str, current_user: User = Depends(get_current_user)):
    with SessionLocal() as db:
        task = Task(description=description, owner_id=current_user.id)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

# Get tasks
@app.get("/tasks/")
def get_tasks(current_user: User = Depends(get_current_user)):
    with SessionLocal() as db:
        tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()
        return tasks

# Mark task as completed
@app.post("/tasks/{task_id}/complete/")
def complete_task(task_id: int, current_user: User = Depends(get_current_user)):
    with SessionLocal() as db:
        task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        completed_task = CompletedTask(task_id=task.id, completed_by=current_user.id)
        db.add(completed_task)
        db.commit()
        db.refresh(completed_task)
        return {"message": "Task marked as completed"}

# ... Other task-related endpoints ...
