from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Street(Base):
    __tablename__ = 'streets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    
    # Foreign key to link to the Location (one-to-many)
    location_id = Column(Integer, ForeignKey('locations.id'))
