# def function1():
#     print("Subscribe now")


# func2 = function1
# del function1
# func2()

# *******************

# return function


# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum


# a = funcret(1)
# print(a)

# *******************

# def executor(func):
#     func("this")


# executor(print)

# *******************
"""

* Decorators are functions that take another function as an argument, and their purpose is to
   modify the other function without changing it.

* The decorator can be said as a modification to the external layer of function,
  as it does not make any change in its structure.
* What a decorator does is, it takes a function and insert some new functionality in it
  without changing the function itself.
* Using decorator we can run our code before and after the function passed as argument

There are two ways to write a Python decorator:
i) We can pass our function to the decorator as an argument, thus define a function
    and pass it to our decorator.
ii) We can simply use the @decorator_name  before the function we'd like to decorate.

There are many Built_in decorators like setter, getter, property etc

"""

# here we are making our own decorator


def dec1(func1):
    def now_exec():
        print("Executing now")
        func1()
        print("Executed")

    return now_exec


@dec1
def who_is_harry():
    print("Harry is a good boy")


# who_is_harry = dec1(who_is_harry)      # way 1

who_is_harry()  # way 2 by using @dec1

# using @dec1 ,  who_is_harry automatically call dec1 function with passing itself as argument
