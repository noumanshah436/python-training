# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created

# **************************

# Order of Variable scope
# LEGB rule (access local first , otherwise look for enclosing ,
#           otherwise look for Global , otherwise look for Built-in )

# L = Local
# E = Enclosing
# G = Global
# B = Built-in

# **************************

name = "Bro"  # global scope (available inside & outside functions)


def display_name():
    name = "Code"  # local scope (available only inside this function)
    print(name)  # access loacal first, if it is declared here


display_name()
print(name)


# ****************************
#
# The global Keyword
# Normally, when you create a variable inside a function,
# that variable is local, and can only be used inside that function.
#
# Using global keyword we can
# 1)  create a global variable inside a function
# 2)  access or change global variable inside a function

# **********
# 1) create a global variable inside a function

def my_func1():
    global var
    var = 20


my_func1()
print("var value is ", var)

# ************
# 2) access or change a global variable inside a function.

x = "Chair"


def my_func2():
    global x
    x = "Desk"


my_func2()
print("I am " + x)

# *********************************************
