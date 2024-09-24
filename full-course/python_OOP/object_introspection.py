""" Introspection can be said as the ability to recognize the object along with all its details,
    such as id or location at runtime.

    type(object)       type of our object,
    id(object)

    o = MyClass()
    print(dir(o))    check the attributes that our object is composed of
*************************************
Types of introspects:-
Some of the other common Introspects:

Functions	    Working
***********************************
hasattr()	    It checks if an object has an attribute.
getattr()	    It returns the contents of an attribute if there are some.
repr()	        It returns the string representation of an object
vars()	        It checks all the instance variables of an object
issubclass()	This function checks that if a specific class is a derived class of another class.
isinstance()	It checks if an object is an instance of a specific class.
__doc__	        This attribute gives some documentation about an object
__name__	    This attribute holds the name of the object
callable()	    This function checks if an object is a function
help()	        It checks what other functions do
    """


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.age= 25
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
# print(skillf.email)
# o = "this is a string"
# print(type(o))
# print(dir(skillf))
# print(id("that that"))

# print(hasattr(skillf, "fname"))
# print(getattr(skillf, "fname"))
# print(repr(skillf))
# print(vars(skillf))
help()
# help(getattr)


# import inspect
#
# print(inspect.getmembers(skillf))

# print(inspect.getmembers(skillf))
# print(inspect.getmembers(skillf))
# print(inspect.getmembers(skillf))
# print(inspect.getmembers(skillf))
