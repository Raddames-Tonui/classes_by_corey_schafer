class Employee:
    
    # class variables
    all_employees = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay): 
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + "@gmail.com"
        Employee.all_employees += 1 
    
    def __repr__(self) -> str:
        return "Employee('{}', {}, {})".format(self.fname, self.lname, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        raise TypeError("Addition can only be performed between Employee instances")
    
    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.pay - other.pay
        raise TypeError("Subtraction can only be performed between Employee instances")

    def fullname(self): 
        return "{} {}".format(self.fname, self.lname)
    
    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

# Creating instances and printing them outside the class definition
emp_1 = Employee("Raddames", "Tonui", 60000)
emp_2 = Employee("Ian", "Kibet", 30000)
emp_3 = Employee("John", "Doe", 40000)

# This will use __repr__ method
print(repr(emp_1))  # Employee('Raddames', 'Tonui', 60000)
print(repr(emp_2))  # Employee('Ian', 'Kibet', 30000)

# This will print the __str__ dunder method
print(emp_2)        # Ian Kibet - Ian.Kibet@gmail.com
print(str(emp_3))   # John Doe - John.Doe@gmail.com
print(emp_1 + emp_3) # 100000 adds emp_1 and emp_3 through __add __
print(emp_1 - emp_3) # 20000
