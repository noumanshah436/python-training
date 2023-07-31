# Public Access Modifier       var = "public"   (easily accessible from any part of the program. )
# Protected Access Modifier    _var ="protected"  (only accessible to a class derived from it)
# Private Access Modifier      __private = "private"


# Name mangling in Python:
# Python does not have any strict rules when it comes to public, protected or private, like java.
# So, to protect us from using the private attribute in any other class, Python does name mangling,
# which means that every member with a double underscore will be changed to object._class__variable
# when trying to call using an object.
# The purpose of this is to warn a user, so he does not use any
# private class variable or function by mistake without realizing its states.
#
# The use of single underscore and double underscore is just a way of name mangling because Python does
# not take the public, private and protected terms much seriously so we have to use our naming conventions
# by putting single or double underscore to let the fellow programmers know which class they
# can access or which they can't.

class Employee:
    no_of_leaves = 8
    public = 8  # public
    _protected = 9
    __private = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def print_modifiers(self):
        return f"Protected: {self._protected}. Private {self.__private} "

    @property
    def protec(self):
        return self._protec


emp = Employee("harry", 343, "Programmer")

print(emp._Employee__private)  # access private member using name_mangling
print(emp._protected, "or", emp._protected)  # access protected member

# print(emp.print_details())
print(emp.print_modifiers())

# ********************************
