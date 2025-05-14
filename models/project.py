from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    start_date = Column(String(25), nullable=True)
    end_date = Column(String(25), nullable=True)

    # Foreign key to link to the Employer (one-to-many)
    location_id = Column(Integer, ForeignKey('locations.id'))

    employer_id = Column(Integer, ForeignKey('employers.id'))


    location = relationship('Location', back_populates='projects')

    # One-to-many: one location -> many employers
    employers = relationship('Employer', back_populates='project')
    # One-to-many: one project -> many employees
    employees = relationship('Employee', back_populates='project')