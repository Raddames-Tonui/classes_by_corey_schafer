# 1. classes - blueprint of creating objects
# 2. objects - instance of a class
    #instance - single occurence of a class
# 3. method - function inside a class
# 4. attributes - variables defined inside a class 
        # instance attribute => hold different data for different instances in  the class
        # class attribute  => All the instances in the class will have similar data
# 5. __init__
# 6. Inheritance - a mechanism where a child  class inherits from the parent class
# 7. Abstraction - hiding complexity of a code


class Animals:  # Class name
    species = "mammals"  # Class attribute

    def __init__(self, name, age, domestic=False, wild=False):
         #  creating Instance attributes
        self.name = name 
        self.age = age 
        self.domestic = domestic 
        self.wild = wild  
    def printer(self):  # Method
        print(f"The animal's name is {self.name} and its species is {self.species}")

    def print_domestic_status(self):  # Method to print domestic status
        print(f"Is the animal domestic? {'Yes' if self.domestic else 'No'}")

    def using_super(self):
        print("This is super from parent super class")

class Human(Animals):
    def males(self):
        print(f"{self.name} is a male")
    
    def using_super(self):
        super().using_super()
        print("This is super from child class")

# Creating objects
dog = Animals("Bosco", 12, True, False)
dog.printer()
dog.print_domestic_status()

Warthog = Animals("Billy", 4, False, True)
Warthog.printer()
Warthog.print_domestic_status()

child = Human("Tonui", 12)
child.printer()
child.males()
child.using_super()