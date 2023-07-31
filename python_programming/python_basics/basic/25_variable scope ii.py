l = 10  # Global

# def function1(n):
#     # l = 5  # Local
#     m = 8  # Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
#
# function1("This is me")
# print(m)


# *******************************
"""
when we write( global var ) inside a function, it will first look outside if there is any
    global variable with that name:

if present globally ->>>>  use that variable
if not present globally ->>>  make global variable outside all functions

( if we declare var with global, inside a nested function, this will also make it outside the parent function)

"""


def harry():  # nested function
    x = 20  # local variable

    def rohan():
        global x  # make global variable x outside of nested functions (as there is no one global with same name)
        x = 88

    print("before calling rohan()", x)  # 20 (as x in rohan is global and x in harry is local, so it will use local )
    rohan()
    print("after calling rohan()", x)  # 20


harry()
print(x)  # 88
