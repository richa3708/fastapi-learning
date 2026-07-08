from fastapi import FastAPI
from app.routers import employees
from app.database import Base, engine
from app.models.employee import Employee

app = FastAPI()

app.include_router(employees.router)

# Base.metadata.create_all(bind=engine)