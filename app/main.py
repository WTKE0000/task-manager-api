from fastapi import FastAPI
from app.routes import tasks

app = FastAPI(title="Task Manager API", version="0.1.0")

app.include_router(tasks.router)

@app.get("/")
def root():
    return{"message":"Task Manager App"}

@app.get("/health")
def health():
    return{"status":"ok"}