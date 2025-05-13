from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Employer(Base):
    __tablename__ = 'employers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    
    location_id = Column(Integer, ForeignKey('locations.id'))
    
    # One-to-many relationship: An Employer has many Employees
    employees = relationship('Employee', back_populates='employer')

    # Many-to-one relationship: An Employer belongs to one Location
    location = relationship('Location', back_populates='employers')
