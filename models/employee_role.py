from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class EmployeeRole(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    employees = relationship('Employee', secondary='employee_role_association', back_populates='roles')