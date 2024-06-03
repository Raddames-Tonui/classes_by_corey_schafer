class Employee:
    def __init__(self,fname,lname, pay): 
        self.fname = fname
        self.lname= lname
        self.pay = pay
    
    def fullname(self): 
        return "{} {}".format(self.fname, self.lname)
    
    def email_address(self):
        return (self.fname + "." + self.lname + "@gmail.com").lower()

# initializing class instances

emp_1 = Employee("Raddames", "Tonui", 60000)
emp_2 = Employee("ian", "Kibet", 30000)
emp_3 = Employee("John", "Doe", 40000)

print(Employee.fullname(emp_1))  # similar to  emp_1.fullname()
print(emp_3.fullname()) 
print(emp_1.pay) # 60000
print(emp_2.email_address()) # ian.kibet@gmail.com

print(emp_1.__dict__) # {'fname': 'Raddames', 'lname': 'Tonui', 'pay': 60000}