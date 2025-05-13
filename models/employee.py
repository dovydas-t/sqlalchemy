from sqlalchemy import Column, ForeignKey, Integer, String, Date, func
from sqlalchemy.orm import relationship
from models.base import Base

# Lentele
class Employee(Base):
    __tablename__ = 'darbuotojai'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    last_name = Column(String(25))
    date_of_birth = Column(Date)
    position = Column(String(25))
    salary = Column(Integer)
    hire_date = Column(Date, default=func.current_date())
    age = Column(Integer, default=18)

     # Foreign key to link to the Employer (one-to-many)
    employer_id = Column(Integer, ForeignKey('employers.id'))

    # Relationship to Employer (one employee belongs to one employer)
    employer = relationship('Employer', back_populates='employees')

    # Many-to-many relationship with Role
    roles = relationship('Role', secondary='employee_role_association', back_populates='employees')

    def __repr__(self):
        return (
            f"<Employee("
            f"id={self.id}, "
            f"name={self.name}, "
            f"last_name={self.last_name}, "
            f"date_of_birth={self.date_of_birth}, "
            f"position={self.position}, "
            f"salary={self.salary}, "
            f"hire_date={self.hire_date})>"
        )
    
    def __str__(self):
        return (
            f"ID: {self.id}\t"
            f"Name: {self.name}\t"
            f"Last Name: {self.last_name}\n"
            f"\tDate of Birth: {self.date_of_birth}\t"
            f"Position: {self.position}\t"
            f"Salary: {self.salary}\t"
            f"Hire Date: {self.hire_date}"
        )
    
employee_table_name = Employee.__tablename__