from fastapi import FastAPI
from app.routers import employees
from app.database import Base, engine
from app.models.employee import Employee
from app.routers import auth

app = FastAPI()

app.include_router(employees.router)
app.include_router(auth.router)

# Base.metadata.create_all(bind=engine)