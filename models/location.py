from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=True)

    # One-to-many: one location -> many employers
    employers = relationship('Employer', back_populates='location')

    # One-to-many: one location -> many projects
    projects = relationship('Project', back_populates='location')

    # One-to-many: one location -> many streets
    streets = relationship('Street', back_populates='location')