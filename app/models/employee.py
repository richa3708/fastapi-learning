from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Employee(Base):
  __tablename__ = "employees"

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  email = Column(String(255), unique=True, nullable=False)
  password = Column(String(255), nullable=False)
  age = Column(Integer, nullable=False)
  department = Column(String(100), nullable=False)
  active = Column(Boolean, default=True)