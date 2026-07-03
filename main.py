from fastapi import FastAPI, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Employee(BaseModel):
    name: str =  Field(min_length=3, max_length=50)
    age: int = Field(gt=18, lt=60)
    department: str
    email: Optional[str] = None
    active: bool = True

employees = [
    {
        "id": 1,
        "name": "Richa",
        "age": 26,
        "department": "Engineering",
        "active": True
    },
    {
        "id": 2,
        "name": "Disha",
        "age": 30,
        "department": "HR",
        "active": True
    },
    {
        "id": 3,
        "name": "Shubham",
        "age": 28,
        "department": "Finance",
        "active": False
    }
]


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee):
    new_employee = employee.model_dump()
    new_employee["id"] = len(employees) + 1
    employees.append(new_employee)
    return {
        "message": "Employee created successfully",
        "employee": new_employee
    }

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"message": "Employee not found!"}

@app.put("/employees/{employee_id}")
def update_employee(employee_data: Employee, employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            new_employee = employee_data.model_dump()
            employee.update(new_employee)
            return {
                "message": "Employee updated successfully",
                "employee": employee
            }
    return {"message": "Employee not found!"}

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            return {
                "message": "Employee deleted successfully"
            }
    return {"message": "Employee not found!"}

# @app.get("/")
# def home():
#     return {"message": "Hello Richa! Welcome to FastAPI"}

# @app.get("/about")
# def about():
#     return{"framework": "FastAPI"}

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}

# @app.get("/search")
# def search(name: str):
#     return {"name": name}