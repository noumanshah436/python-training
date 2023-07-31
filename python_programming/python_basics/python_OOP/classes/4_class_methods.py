# calling, class method with object or class is same
# good practice is to call it using class name

# 1) The class method only has access to cls argument, it cannot modify object instance state.
# However, class methods can still modify class state that applies to all instances of the class.
# So a class method automatically recognizes a class, so the only parameter that remaines to be passed
# is the function that needs conversion.



# 2) A @classmethod Decorator is a built-in function in Python. It can be applied to any method of the class.
#   We can change the value of class variables using this method too.

# The classmethod() is an inbuilt function in Python, which returns a class method for a given function.

# 3) Python class method is a way to define a function for the Python class.
# It receives the class as an implicit first argument. Using @classmethod decorator,
# it is possible to create as many constructors for a class that behaves like a factory constructor.

#
# Syntax:
#
# class myClass:
#     @classmethod
#     def myfunc (cls, arg1, arg2, ...):
#                           ....

# myfunc defines the function that needs to be converted into a class method
# returns: @classmethod returns a class method for function.

# ****************************************

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname  # constructing object (create instance variables)
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls, leaves):  # csl -> class of the object
        cls.no_of_leaves = leaves

        # if we do not use cls keyword, this variable will not do anything to class or object variables
        # it will be just a block scope temporary variable

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")
nouman = Employee("Nouman", 300, "Student")


Employee.change_leaves(20)
harry.change_leaves(34)
print(harry.__dict__)

print(harry.no_of_leaves)
print(Employee.no_of_leaves)



# we can call class method using instance of the class but it can only change class attributes

# Class methods are useful when you want to operate on class-level attributes or perform actions related to the class itself, rather than specific instances. However, keep in mind that calling class methods using instances is generally less common, as class methods are usually called using the class itself (e.g., MyClass.class_method()).
