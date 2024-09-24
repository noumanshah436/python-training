# in constructor we can create instance of object using self keyword.
# if we do not use self (object itself) with variable, it will not belong to object ,
#          rather it just block scope temporary variable
# we can only create instances of object usign

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):    # self means object itself
        self.name = aname  # constructing object (create instance variables)
        self.salary = asalary
        self.role = arole
        temp_variable = 10     # not an instance or class variable
        print(temp_variable)

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")    # self is passed automatically as argument

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# harry.shirt ="blue"    # make another instance of harry

print(harry.salary)
