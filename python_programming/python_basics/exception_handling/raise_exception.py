# First, let us briefly go over the meaning of the word exception. The exception is an error that
# halts the program's normal functioning and displays an error onto the screen. While the try and
# except block are for handling exceptions, the raise keyword, on the contrary, is to raise an exception.


# Syntax of raise keyword is:

# if test_condition:
#   raise EXCEPTION_CLASS_NAME


# Taking a simple usage example:
# raise ZeroDivisionError

# *******************************************************

# a = input("What is your name")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")
# 1000 lines taking 1 hour

# Task - Write about 2 built in exception

c = input("Enter your name")
try:
    print(a)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")

