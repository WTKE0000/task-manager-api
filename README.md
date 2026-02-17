# Task Manager API (FastAPI + SQLite)

A simple backend REST API built with FastAPI and SQLAlchemy.

## Features

- Create tasks
- List all tasks
- Get task by ID
- Update task
- Delete task
- SQLite database persistence
- Proper 404 error handling

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Run Locally

python -m venv venv
# Windows:
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
uvicorn app.main:app --reload

## API Endpoints

POST /tasks  
GET /tasks  
GET /tasks/{id}  
PUT /tasks/{id}  
DELETE /tasks/{id}

Docs available at:
http://127.0.0.1:8000/docs
