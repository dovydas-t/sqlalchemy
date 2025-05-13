from sqlalchemy.orm import Session
from models.employee import Employee
from models.employer import Employer
from models.employee_role import EmployeeRole


def create_employee(db: Session, employee_data: dict) -> Employee:
    """
    Function to create a new employee in the given database by given keys and values.
    'name' is required, others are optional.
    Returns the created Employee object.
    """
    new_employee = Employee(**employee_data)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


def get_employee_by_id(db: Session, employee_id: int) -> Employee:
    """
    Function to get data from given database by given id.
    Returns the Employee object if found, otherwise None.
    """
    return db.query(Employee).filter(Employee.id == employee_id).first()


def update_employee(db: Session, employee_id: int, updates: dict) -> Employee:
    """
    Function to update an employee with given details as keys and values into given database by given id.
    Returns the updated Employee object.
    """
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        for key, value in updates.items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int) -> bool:
    """
    Function to delete an employee from the given database by given id.
    Returns True if deleted successfully, otherwise False.
    """
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False


def get_all_employees(db: Session) -> list[Employee]:
    """
    Function to get all employees from the given database.
    Returns a list of Employee objects.
    """
    return db.query(Employee).all()


def create_employer(db: Session, employer_data: dict) -> Employer:
    """
    Function to create a new employer in the given database by given keys and values.
    'name' is required, others are optional.
    Returns the created Employer object.
    """
    new_employer = Employer(**employer_data)
    db.add(new_employer)
    db.commit()
    db.refresh(new_employer)
    return new_employer


def get_all_employers(db: Session) -> list[Employer]:
    """
    Function to get all employers from the given database.
    Returns a list of Employer objects.
    """
    return db.query(Employer).all()


def assign_employee_to_employer(db: Session, employee_id: int, employer_id: int) -> bool:
    """
    Function to assign an employee to an employer in the given database.
    Returns True if assigned successfully, otherwise False.
    """
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    employer = db.query(Employer).filter(Employer.id == employer_id).first()
    if employee and employer:
        employee.employer_id = employer.id
        db.commit()
        return True
    return False


def get_employees_by_employer_id(db: Session, employer_id: int) -> list[Employee]:
    """
    Function to get all employees for a given employer ID from the given database.
    Returns a list of Employee objects.
    """
    return db.query(Employee).filter(Employee.employer_id == employer_id).all()


def remove_employee_from_employer(db: Session, employee_id: int) -> bool:
    """
    Function to remove an employee from their employer in the given database.
    Returns True if removed successfully, otherwise False.
    """
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        employee.employer_id = None
        db.commit()
        return True
    return False

def get_employed_employees(db: Session) -> list[Employee]:
    """
    Function to get all employed employees from the given database.
    Returns a list of Employee objects.
    """
    return db.query(Employee).filter(Employee.employer_id != None).all()

def create_role(db: Session, role_name: str) -> EmployeeRole:
    role = EmployeeRole(name=role_name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def get_all_roles(db: Session) -> list[EmployeeRole]:
    return db.query(EmployeeRole).all()


def assign_roles_to_employee(db: Session, employee_id: int, role_names: list[str]) -> Employee:
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        roles = db.query(EmployeeRole).filter(EmployeeRole.name.in_(role_names)).all()
        employee.roles = roles
        db.commit()
        db.refresh(employee)
    return employee


def remove_all_roles_from_employee(db: Session, employee_id: int) -> bool:
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        employee.roles = []
        db.commit()
        return True
    return False