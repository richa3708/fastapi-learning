from fastapi import APIRouter, status
from app.schemas.employee import Employee
from app.data.employees import employees

router = APIRouter()

@router.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee):
    new_employee = employee.model_dump()
    new_employee["id"] = len(employees) + 1
    employees.append(new_employee)
    return {
        "message": "Employee created successfully",
        "employee": new_employee
    }

@router.get("/employees")
def get_employees():
    return employees

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"message": "Employee not found!"}

@router.put("/employees/{employee_id}")
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

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            return {
                "message": "Employee deleted successfully"
            }
    return {"message": "Employee not found!"}