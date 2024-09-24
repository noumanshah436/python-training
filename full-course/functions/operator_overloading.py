# Operator overloading means to give new meanings to an operator. In simple words,
# it means to assign new functionality to an operator beyond its normal functioning

# Python Dunder Methods Or Special Functions:
# Methods starting with a double underscore ( __ ) and ending with a double underscore ( __ ) represents dunder methods.
# Dunder methods in Python are special methods. such as __init__ method that every Class has.
# In Python, Dunder methods are used for operator overloading and for customizing the behaviour of some other
# function.


# __str__ and __repr__ functions
# Both of these built-in methods are used to return a presentable description about any object
# rather than the default one. The difference in them is the way of writing them. The __str__ method
# is mainly written for the end-user, while __repr__ is written for a developer. It is overridden to
# return a printable string representation of any user-defined class.
#
# Difference between __str__ and __repr__ functions
# 1) If the implementation of __str__ is missing, then __repr__ function is used as a fallback.
#     If the implementation of __repr__ is missing, then there will be no fallback.
# 2) If __repr__ function is returning the String representation of the object,
#     we can skip the implementation of __str__ function.
# 3) The priority of __str__ is higher than __repr__.

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Nouman", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(emp1)
print(repr(emp1))
print(str(emp1))
