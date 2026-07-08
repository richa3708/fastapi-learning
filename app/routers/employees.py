from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.dependencies import get_db
from app.models.employee import Employee as EmployeeModel
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse
)

router = APIRouter()

@router.post(
  "/employees", 
  response_model=EmployeeResponse,
  status_code=status.HTTP_201_CREATED
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    db_employee = EmployeeModel(
        name=employee.name,
        email=employee.email,
        age=employee.age,
        department=employee.department,
        active=employee.active,
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee

@router.get("/employees", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(EmployeeModel).all()
    return employees

@router.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(EmployeeModel).filter(
        EmployeeModel.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee: EmployeeCreate,
    employee_id: int,
    db: Session = Depends(get_db)
):
    db_employee = db.query(EmployeeModel).filter(
        EmployeeModel.id == employee_id
    ).first()

    if not db_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.age = employee.age
    db_employee.department = employee.department
    db_employee.active = employee.active

    db.commit()
    db.refresh(db_employee)

    return db_employee

@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.query(EmployeeModel).filter(
        EmployeeModel.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }