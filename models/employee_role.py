from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db_connection import Base

class EmployeeRole(Base):
    __tablename__ = 'employee_roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    employees = relationship('Employee', secondary='employee_role_association', back_populates='roles')