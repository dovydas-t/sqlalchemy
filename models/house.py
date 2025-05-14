from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to link to the Street (one-to-many)
    street_id = Column(Integer, ForeignKey('streets.id'))

    name = Column(String(255), nullable=True)
