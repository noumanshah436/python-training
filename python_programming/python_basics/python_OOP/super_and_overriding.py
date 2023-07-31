# when we access child class variables using its object it looks that variable in following order
# 1) first it looks instance variable of that child class (in its __init__ method , etc)
# 2) second it looks instance variable of its parent class ( if any )
# 3) third it looks class variable of that child class (in __init__ method , etc)
# 4) forth it looks class variable of its parent class

# *************************************

# if we override __init__ constructor in child class and do not call super().__init__() here ,
#   the super class constructor will not be executed, hence we cannot use instance variables we created in super class.

# if we call super().__init__() in the the end of child class __init__ ,
#  it will execute at the end of __init__ and will override variables with same name of child class

# *************************************


class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        print("in constructor of class A")
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()
        print("in constructor of class B")
        # print(super().classvar1)
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"


a = A()
b = B()

print(b.special)
print(b.var1)
print(b.classvar1)
