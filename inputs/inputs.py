def name_input() -> str:
    """
    Function to get a valid name from user input.
    Returns the name as a string.
    """
    while True:
        name = input("\tEnter name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid input. Please enter a valid name.")

def last_name_input() -> str:
    """
    Function to get a valid last name from user input.
    Returns the last name as a string.
    """
    while True:
        last_name = input("\tEnter last name: ")
        if last_name == "":
            break
        elif last_name.isalpha():
            return last_name
        else:
            print("Invalid input. Please enter a valid last name.")

def date_of_birth_input() -> str:
    """
    Function to get a valid date of birth from user input.
    Returns the date of birth as a string in YYYY-MM-DD format.
    """
    while True:
        date_of_birth = input("\tEnter date of birth (YYYY-MM-DD): ")
        if date_of_birth == "":
            break
        try:
            year, month, day = map(int, date_of_birth.split('-'))
            if 1 <= month <= 12 and 1 <= day <= 31:
                return date_of_birth
            else:
                print("Invalid date. Please enter a valid date.")
        except ValueError:
            print("Invalid format. Please enter the date in YYYY-MM-DD format.")

def position_input() -> str:
    """
    Function to get a valid position from user input.
    Returns the position as a string.
    """
    while True:
        position = input("\tEnter position: ")
        if position == "":
            break
        if position.isalpha():
            return position
        else:
            print("Invalid input. Please enter a valid position.")

def salary_input() -> float:
    """
    Function to get a valid salary from user input.
    Returns the salary as a float.
    """
    while True:
        salary = input("\tEnter salary: ")
        if salary == "":
            break
        try:
            salary = float(salary)
            if salary >= 0:
                return salary
            else:
                print("Invalid input. Salary cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number for salary.")

def hire_date_input() -> str:
    """
    Function to get a valid hire date from user input.
    Returns the hire date as a string in YYYY-MM-DD format.
    """
    while True:
        hire_date = input("\tEnter hire date (YYYY-MM-DD) or press Enter to use current date: ")
        if hire_date == "":
            break  # Default to current date
        try:
            year, month, day = map(int, hire_date.split('-'))
            if 1 <= month <= 12 and 1 <= day <= 31:
                return hire_date
            else:
                print("Invalid date. Please enter a valid date.")
        except ValueError:
            print("Invalid format. Please enter the date in YYYY-MM-DD format.")

###########################

def get_employee_data() -> dict:
    """
    Function to get employee data from user input.
    Returns a dictionary with employee details.
    """
    print("\nEnter employee details:")
    name = name_input()
    last_name = last_name_input()
    date_of_birth = date_of_birth_input()
    position = position_input()
    salary = salary_input()
    hire_date = hire_date_input()
    employee_data = {"name": name}
    if last_name:
        employee_data["last_name"] = last_name
    if date_of_birth:
        employee_data["date_of_birth"] = date_of_birth
    if position:
        employee_data["position"] = position
    if salary:
        employee_data["salary"] = salary
    if hire_date:
        employee_data["hire_date"] = hire_date

    
    return employee_data

def get_employer_data() -> dict:
    """
    Function to get employer data from user input.
    Returns a dictionary with employer details.
    """
    print("\nEnter employer details:")
    name = name_input()
    employer_data = {"name": name}
    
    return employer_data

def id_input() -> int:
    """
    Function to get employee/employer ID from user input.
    Returns the ID as an integer.
    """
    while True:
        try:
            input_id = int(input("\tEnter ID: "))
            return input_id
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

if __name__ == "__main__":
    employee_data = get_employee_data()
    print("Employee data collected:\n", employee_data)
