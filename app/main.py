from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="FastAPI MongoDB CRUD API",
    description="CRUD operations using FastAPI and MongoDB",
    version="1.0"
)

app.include_router(router)