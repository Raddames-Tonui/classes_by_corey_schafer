class Employee:
    
    # class variables
    all_employees = 0
    raise_amount = 1.04

    def __init__(self,fname,lname, pay): 
        self.fname = fname
        self.lname= lname
        self.pay = pay
        self.email = fname + "." + lname + "@gmail.com"
        Employee.all_employees += 1  

    def fullname(self): 
        return "{} {}".format(self.fname, self.lname) # alternative   self.fulname = fname + lname

    
    def apply_raise(self): # this would change each instance differently as long as it's called individually.
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
emp_1 = Employee("Raddames", "Tonui", 60000)
emp_2 = Employee("ian", " Kibet", 30000)
emp_3 = Employee("John", "Doe", 40000)


print(Employee.fullname(emp_1))  # similar to  emp_1.fullname()
print(emp_1.fullname())

emp_1.apply_raise()
print(emp_1.pay) # changes only but the other employees will have the same pay
print(emp_2.pay)
print(Employee.all_employees) # after each instance it will be added
