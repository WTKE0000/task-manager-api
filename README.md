# Task Manager REST API

A modular RESTful backend API built using FastAPI and SQLAlchemy with SQLite persistence.

## Architecture

The project follows a clean modular structure:

app/
  main.py
  database.py
  models/
    task.py
    task_db.py
  routes/
    tasks.py

## Features

- Create tasks
- List all tasks
- Get task by ID
- Update tasks
- Delete tasks
- SQLite database persistence
- Proper 404 error handling
- Dependency-based database sessions

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Why FastAPI?

FastAPI provides:
- Automatic API documentation
- Strong data validation with Pydantic
- High performance async-ready framework

## Running Locally

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload

Docs available at:
http://127.0.0.1:8000/docs
