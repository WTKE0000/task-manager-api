from fastapi import APIRouter, HTTPException
from app.models.task import Task, TaskCreate, TaskUpdate
from typing import List


router = APIRouter(prefix="/tasks", tags=["Tasks"])


tasks_db = []
task_id_counter = 1


@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter

    new_task = Task(id=task_id_counter, title=task.title, description=task.description)

    tasks_db.append(new_task)
    task_id_counter = 1

    return new_task

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter

    new_task = Task(
        id = task_id_counter,
        title= task.title,
        description=task.description
    )

@router.get("/", response_model=List[Task])
def list_tasks():
    return tasks_db

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
        raise HTTPException(status_code=404, details="Task not found")
    
@router.put("/{task_id}", response_model= Task)
def update_task(task_id: int, update: TaskUpdate):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task = Task(
                id = task.id,
                title=update.title if update.title is not None else task.title,
                description=update.description if update.description is not None else task.description,
            )
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=400, detail="Task not found")
@router.delete("/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate (tasks_db):
        if task.id == task.id:
            tasks_db.pop(i)
            return {"deleted": True, "id": task_id}
    raise HTTPException(status_code=404, detail="task not found")