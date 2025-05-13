from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Employer(Base):
    __tablename__ = 'employers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    
    # One-to-many relationship: An Employer has many Employees
    employees = relationship('Employee', back_populates='employer')
