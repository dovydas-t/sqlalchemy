from database.db_connection import database as db_name
from models.employee import employee_table_name
from tabulate import tabulate

def show_menu():
    print("\n" + "-" * 50)
    print("\nWelcome to the Employee Management System")
    print(f"Database: {db_name}\tTable: {employee_table_name}\n")
    print("Please choose an option:")
    print("\t1. Add new employee")
    print("\t2. Update employee details")
    print("\t3. Delete employee")
    print("\t4. View all employees")
    print("\t5. Search employee")
    print("")
    print("\t6. Create new employer")
    print("\t7. View all employers")
    print("\t8. Assign employee to employer")
    print("\t9. View all employees of an employer")
    print("\t10. Remove employee from employer")
    print("\t11. Show all employed employees")
    print("")
    print("\t98. restart database")
    print("\t99. refresh database")
    print("")
    print("\t0. Exit")

def show_employees(employees_list: list) -> None:
    print("\nEmployees:")
    print(tabulate(
        [[emp.id, emp.name, emp.last_name, emp.date_of_birth, emp.position, emp.salary, emp.hire_date] for emp in employees_list],
        headers=["ID", "Name", "Last Name", "Date of Birth", "Position", "Salary", "Hire Date"],
        tablefmt="github"
    ))

def show_employee(e: object) -> None:
    print("\nEmployee:")
    print(tabulate(
        [[e.id, e.name, e.last_name, e.date_of_birth, e.position, e.salary, e.hire_date]],
        headers=["ID", "Name", "Last Name", "Date of Birth", "Position", "Salary", "Hire Date"],
        tablefmt="github"
    ))

def show_employers(employers_list: list) -> None:
    print("\nEmployers:")
    print(tabulate(
        [[emp.id, emp.name] for emp in employers_list],
        headers=["ID", "Name"],
        tablefmt="github"
    ))

def show_employees_of_employer(employed_list: list) -> None:
    print("\nEmployees of Employer:")
    print(tabulate(
        [[emp.id, emp.name, emp.last_name] for emp in employed_list],
        headers=["ID", "Name", "Last Name"],
        tablefmt="github"
    ))

def show_employed_employees(employed_list: list) -> None:
    print("\nEmployed Employees:")
    print(tabulate(
        [[emp.id, emp.name, emp.last_name, emp.position, emp.salary, emp.employer_id] for emp in employed_list],
        headers=["ID", "Name", "Last Name", "Position", "Salary", "Employer ID"],
        tablefmt="github"
    ))


if __name__ == "__main__":
    show_menu()
