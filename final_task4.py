import json

# employee_list = [{'name' : 'Nelson C.P', 'department' : 'Sales', 'position' : 'Manager', 'salary' : '20000', 'phone' : '0983547625'},{'name' : 'Lopez C.I', 'department' : 'Marketing', 'position' : 'Analyst', 'salary' : '15000', 'phone' : '0689348120'},{'name' : 'Anderson W.T', 'department' : 'Accounting', 'position' : 'Manager', 'salary' : '15000', 'phone' : '0735478294'},{'name' : 'Diaz Q.D', 'department' : 'Sales', 'position' : 'Consultant', 'salary' : '20000', 'phone' : '0986783620'}, {'name' : 'Long X.T', 'department' : 'Logistics', 'position' : 'Manager', 'salary' : '20000', 'phone' : '0687209538'}]

employees = "data.json"

# with open(employees, 'w') as file:
#     json.dump(employee_list, file, indent=4)
def load_data():
    try:
        with open(employees, 'r') as file:
            return json.load(file)
    except FileNotFoundError as msg:
        print(msg)

def save_data(data):
    with open(employees, 'w') as file:
        json.dump(data, file, indent=4)

def view_all(employees):
    if not employees:
        print("Empty list.")
    i = 1
    for person in employees:
        print(f"ID:: {i} - {person}")
        i+=1

def add_employee(employees): 
    name = input("Enter name and initials :: ").strip()
    

    for person in employees:
        if person['name'].lower() == name:
            print("Employee with that name is already existing.")
            return
    
    
    while True:
        flag = True 
        phone = input("Enter phone number :: ").strip()
        for person in employees:
            if person['phone'] == phone:
                print("This phone number is already in use.")
                flag = False
                break
        if flag:
            break

    department = input("Відділ: ")
    position = input("Посада: ")
    salary = input("Зарплата: ")

    new_employee = {
        "name": name,
        "department": department,
        "position": position,
        "salary": salary,
        "phone": phone,
    }

    employees.append(new_employee)
    save_data(employees)


def delete_employee(employees):
    while True:
        try:
            id = int(input("Enter ID employee :: "))
            if id < 1 or id > len(employees):
                print("Error ID employee")
                continue
            employees.pop(id - 1)
            break
        except:
            print("Error Value ID")
    save_data(employees)

def transfer_employee(employees):
    while True:
        try:
            id = int(input("Enter ID employee :: "))
            if id < 1 or id > len(employees):
                print("Error ID employee")
                continue
            employees[id -1]['department'] = input("Відділ: ")
            break
        except:
            print("Error Value ID")
    save_data(employees)

def find_by_name(employees):
    name = input("Enter name :: ")
    result = list(filter(lambda x : x['name'].lower() == name.lower(), employees))
    if len(result) == 0:
        print("Employee not found")
    else:
        print(result[0])

def find_by_department(employees):
    department = input("Enter department :: ")
    result = list(filter(lambda x : x['department'].lower() == department.lower(), employees))
    if len(result) == 0:
        print("List Employee is empty")
    else:
        view_all(result)

def get_departments(employees):
    name_departments = list(set(map(lambda x: x["department"], employees)))
    for department in name_departments:
        print(f"{department} :: {len(list(filter(lambda x : x['department'] == department, employees)))} employees")

def get_salary_in_departments(employees):
    name_departments = list(set(map(lambda x: x["department"], employees)))
    for department in name_departments:
        employee_in_department = list(filter(lambda x : x['department'] == department, employees))
        # print(employee_in_department)
        # print(list(map(lambda x: int(x['salary']),employee_in_department)))
        print(f"{department} :: {sum(map(lambda x: int(x['salary']),employee_in_department))} $")

employee_list = load_data()

while True:
    menu = int(input('''
                    --Menu--
            1. Add new employee
            2. Remove employee
            3. Find by name
            4. View all
            5. Find by department
            6. Statistics by department
            7. Report
            8. Sorted Employees
            0. Exit
                    Enter your choice :: '''))
    match menu:
        case 1:
            add_employee(employee_list)
        case 2:
            view_all(employee_list)
            delete_employee(employee_list)
        case 3:
            find_by_name(employee_list)
        case 4:
            view_all(employee_list)
        case 5:
            find_by_department(employee_list)
        case 6:
            choice = int(input('''
                1 - number of employees
                2 - salary departments 
                enter :: '''))
            if choice == 1:
                get_departments(employee_list)
            if choice == 2:
                get_salary_in_departments(employee_list)
        case 7:
            choice = int(input('''
                1 - delete  employees
                2 - transfer the employee 
                enter :: '''))
            if choice == 1:
                view_all(employee_list)
                delete_employee(employee_list)
            if choice == 2:
                view_all(employee_list)
                transfer_employee(employee_list)
        case 8:
            choice = int(input('''
                1 - Departments
                2 - Positions
                enter :: '''))
            if choice == 1:
                view_all(sorted(employee_list, key= lambda x: x['department']))
            if choice == 2:
                view_all(sorted(employee_list, key= lambda x: x['position']))


