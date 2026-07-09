from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=18, lt=60)
    department: str
    email: Optional[str] = None
    active: bool = True
    password: str

class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    department: str
    email: Optional[str]
    active: bool

    model_config = ConfigDict(from_attributes=True)