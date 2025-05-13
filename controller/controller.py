from database.db_connection import SessionLocal

# session = SessionLocal()

from views.user_interface import show_menu
from views.user_interface import show_employees, show_employee
from views.user_interface import show_employers, show_employees_of_employer, show_employed_employees

from inputs.inputs import get_employee_data, id_input
from inputs.inputs import get_employer_data


from database.crud import create_employee, get_all_employees, get_employee_by_id, update_employee, delete_employee
from database.crud import create_employer, get_all_employers, assign_employee_to_employer, get_employees_by_employer_id
from database.crud import remove_employee_from_employer, get_employed_employees

def run():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        match choice:

            case '1':
                employee_data = get_employee_data()
                with SessionLocal() as session:
                    new_employee = create_employee(session, employee_data)
                    if new_employee:
                        print(f"\nEmployee {new_employee.name} added successfully.")
                    else:
                        print("\nFailed to add employee.")

            case '2':
                employee_id = id_input()
                employee_data = get_employee_data()
                with SessionLocal() as session:
                    updated_employee = update_employee(session, employee_id, employee_data)
                    if updated_employee:
                        print(f"\nEmployee {updated_employee.name} updated successfully.")
                    else:
                        print("\nFailed to update employee.")

            case '3':
                employee_id = id_input()
                with SessionLocal() as session:
                    if delete_employee(session, employee_id):
                        print(f"\nEmployee with ID {employee_id} deleted successfully.")
                    else:
                        print("\nFailed to delete employee or employee not found.")

            case '4':
                with SessionLocal() as session:
                    employees_list = get_all_employees(session)
                    if employees_list:
                        show_employees(employees_list)
                    else:
                        print("\nNo employees found.")

            case '5':
                employee_id = id_input()
                with SessionLocal() as session:
                    employee = get_employee_by_id(session, employee_id)
                    if employee:
                        show_employee(employee)
                    else:
                        print("\nEmployee not found.")

            case '6':
                employer_data = get_employer_data()
                with SessionLocal() as session:
                    new_employer = create_employer(session, employer_data)
                    if new_employer:
                        print(f"\nEmployer {new_employer.name} added successfully.")
                    else:
                        print("\nFailed to add employer.")

            case '7':
                with SessionLocal() as session:
                    employers_list = get_all_employers(session)
                    if employers_list:
                        show_employers(employers_list)
                    else:
                        print("\nNo employers found.")
            
            case '8':
                print("\nAssign Employee to Employer")
                print("Please enter the ID of the employee.")
                employee_id = id_input()
                print("Please enter the ID of the employer.")
                employer_id = id_input()
                with SessionLocal() as session:
                    if assign_employee_to_employer(session, employee_id, employer_id):
                        print(f"\nEmployee with ID {employee_id} assigned to Employer with ID {employer_id}.")
                    else:
                        print("\nFailed to assign employee to employer.")

            case '9':
                employer_id = id_input()
                print(f"\nEmployer ID: {employer_id}")

                with SessionLocal() as session:
                    employees_of_employer = get_employees_by_employer_id(session, employer_id)
                    if employees_of_employer:
                        show_employees_of_employer(employees_of_employer)
                    else:
                        print("\nNo employees found for this employer.")
            
            case '10':
                employee_id = id_input()
                with SessionLocal() as session:
                    if remove_employee_from_employer(session, employee_id):
                        print(f"\nEmployee with ID {employee_id} removed from employer.")
                    else:
                        print("\nFailed to remove employee from employer or employee not found.")
            
            case '11':
                with SessionLocal() as session:
                    employed_employees = get_employed_employees(session)
                    if employed_employees:
                        show_employed_employees(employed_employees)
                    else:
                        print("\nNo employed employees found.")


            case '0':
                print("Exiting the program.")
                break


            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run()
