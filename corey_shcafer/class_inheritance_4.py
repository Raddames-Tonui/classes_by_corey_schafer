class Employee:
    def __init__(self, fname, lname, pay): 
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + "@gmail.com"
    
    def fullname(self): 
        return "{} {}".format(self.fname, self.lname)

class Developer(Employee):
    def __init__(self, fname, lname, pay, lang):
        # Call the parent class's __init__ method to initialize fname, lname, and pay
        super().__init__(fname, lname, pay)
        # Initialize the Developer specific attribute
        self.lang = lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        # Call the parent class's __init__ method to initialize fname, lname, and pay
        super().__init__(fname, lname, pay)
        # Initialize the Manager specific attribute, employees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        # Add an employee to the manager's list of employees if not already present
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        # Remove an employee from the manager's list of employees if present
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        # Print the full names of all employees managed by the manager
        for emp in self.employees:
            print("---->", emp.fullname())
            
    
# Creating Developer instances
Dev1 = Developer("James", "Bond", 5000, "Python")
Dev2 = Developer("Charles", "Njonjo", 6000, "Java")
Dev3 = Developer("John", "Doe", 7000, "C++")

# Creating Manager instances
Mng1 = Manager("Raddames", "Tonui", 90000)
Mng2 = Manager("Nicklaus", "Michaelson", 44000, [Dev2])

# Testing Developer instances
print(Dev1.fullname())  # Output: James Bond
print(Dev1.email)       # Output: James.Bond@gmail.com
print(Dev1.lang)        # Output: Python

# Adding Developer instances to Manager
Mng1.add_emp(Dev1)
Mng1.add_emp(Dev3)

# Printing employees managed by Mng1
print("Employees managed by Mng1:")
Mng1.print_employees()  # Output: ----> James Bond ----> John Doe

# Removing an employee
Mng1.remove_emp(Dev1)
print("Employees managed by Mng1 after removal:")
Mng1.print_employees()  # Output: ----> John Doe

# Printing employees managed by Mng2
print("Employees managed by Mng2:")
Mng2.print_employees()  # Output: ----> Charles Njonjo

# Adding Dev1 to Mng2
Mng2.add_emp(Dev1)
print("Employees managed by Mng2 after adding Dev1:")
Mng2.print_employees()  # Output: ----> Charles Njonjo ----> James Bond

# Printing __dict__ of Dev1
print("Dev1 __dict__:", Dev1.__dict__)  # Output: {'fname': 'James', 'lname': 'Bond', 'pay': 5000, 'email': 'James.Bond@gmail.com', 'lang': 'Python'}
print("Mng1 __dict__:", Mng1.__dict__)  # Output: {'fname': 'Raddames', 'lname': 'Tonui', 'pay': 90000, 'email': 'Raddames.Tonui@gmail.com', 'employees': [<__main__.Developer object at 0x...>]}

# Creating an employee not managed by any manager
Emp1 = Employee("Alice", "Smith", 55000)
print(Emp1.fullname())  # Output: Alice Smith
print(Emp1.email)       # Output: Alice.Smith@gmail.com
print(Emp1.pay)         # Output: 55000

# Checking if Emp1 is an instance of Employee
print(isinstance(Emp1, Employee))  # Output: True
print(isinstance(Emp1, Developer))  # Output: False
print(isinstance(Mng1, Developer))  # Output: False

# Checking if Developer is a subclass of Employee
print(issubclass(Developer, Employee))  # Output: True
print(issubclass(Manager, Employee))  # Output: True
print(issubclass(Manager, Developer))  # Output: False
