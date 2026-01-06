# FastAPI MongoDB CRUD API
A simple backend REST API built using FastAPI and MongoDB to perform basic CRUD operations.

---

## Features
- Create, read, update, and delete users
- Automatic request validation using FastAPI
- Asynchronus MongoDB operations

---
## Tech Stack
- Python
- FastAPI
- MongoDB
- Motor (Async MongoDB Driver)
- Pydantic
- Postman
- MongoDB Compass

## API Testing
All APIs were tested using Postman.
Screenshots of successfull requests and database verification are included in the repository.

---

## How to run

1. Start MongoDB
   - net start MongoDB
2. Install libraries
   - pip install -r requirements.txt
3. Run the server
   - uvicorn app.main:app --reload
   - API will be available at:
     http://127.0.0.1:8000/docs
