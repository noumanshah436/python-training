"""
Things to Remember:
1) *args and *kwargs are special keyword which allows function to take variable length argument.
2) *args passes variable number of non-keyword arguments list. (the argument could be a list or tuple.)
3) **kwargs passes variable number of keyword arguments dictionary.
4) *args and **kwargs make the function flexible.
5) order of parameters:  normal , *args  , **kwargs
"""


# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def fun_args(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Ali", "Hammad",
       "Watson", "The programmer"]

normal = "I am a normal Argument and the students are:"

kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}


fun_args(normal, *har, **kw)
