from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base import Base

employee_role_association = Table(
    'employee_role_association', Base.metadata,
    Column('employee_id', Integer, ForeignKey('darbuotojai.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)