from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=18, lt=60)
    department: str
    email: Optional[str] = None
    active: bool = True