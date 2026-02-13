from fastapi import FastAPI

app = FastAPI(title="Task Manager API", version="0.1.0")

@app.get("/")
def root():
    return{"message":"Task Manager App"}

@app.get("/health")
def health():
    return{"status":"ok"}