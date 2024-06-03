class Employee:
    def __init__(self, fname, lname, pay=None):
        self.fname = fname 
        self.lname = lname 
        if pay is None:
            self.pay = 0
        else:
            self.pay = pay  # Pay attribute

    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)  # Computed property for full name

    @property
    def email(self):
        return ("{}.{}@email.com".format(self.fname, self.lname)).lower()  # Computed property for email
    
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(" ")  # Splitting the input name into first and last names
        self.fname = fname  # Updating first name attribute
        self.lname = lname  # Updating last name attribute
    
    @fullname.deleter
    def del_fullname(self):
        print("Deleted name")
        self.fname = None
        self.lname = None

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.pay)  # String representation of Employee object

emp_1 = Employee("Raddames", "Tonui", 60000)
emp_2 = Employee("Jordan", "Peterson", 30000)
print(emp_1.fullname)  # Printing full name of emp_1
print(emp_2.fullname)  # Printing full name of emp_2 (Jordan Peterson initially)
emp_2.fullname = "Joseph Bii"  # Changing the full name of emp_2
print(emp_2.fullname)  # Printing updated full name of emp_2 (Joseph Bii)
print(emp_2.email)  # Printing email of emp_2 (joseph.bii@email.com)
