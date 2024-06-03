from calendar import weekday
import datetime

class Employee:
    all_employees = 0  # Class variable to track the number of employees
    raise_amount = 1.04  # Class variable for the default raise amount

    def __init__(self, fname, lname, pay): 
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + "@gmail.com"
        Employee.all_employees += 1  # Increment the count of all employees

    def fullname(self): # Return the full name of the employee        
        return "{} {}".format(self.fname, self.lname)
    
    def apply_raise(self): # Apply the raise amount to the employee's pay        
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod  # Class method
    def set_raise_amnt(cls, amount):# Set the raise amount for all employees
        cls.raise_amount = amount
        return cls.raise_amount

    @classmethod  # Alternative constructor to create an Employee from a string
    def from_string(cls, empt_str):
        fname, lname, pay = empt_str.split("-")
        return cls(fname, lname, pay)
    
    @staticmethod  # Static method to check if a date is a workday
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Check if a specific date is a workday
my_date = datetime.date(2024, 6, 3)
print(Employee.is_workday(my_date))  # Output: True (June 3, 2024, is a Monday)

# Creating Employee instances
emp_1 = Employee("Raddames", "Tonui", 60000)
emp_2 = Employee("Ian", "Kibet", 30000)
emp_3 = Employee("John", "Doe", 40000)
# Creating an Employee instance from a string
emp_4 = Employee.from_string("Isaac-Kibet-30000")
print(emp_4.fullname())  # Output: Isaac Kibet

# Set a new raise amount for all employees
Employee.set_raise_amnt(1.6)
print(Employee.raise_amount)  # Output: 1.6
print(emp_1.apply_raise())  # Output: 96000 (60000 * 1.6)
