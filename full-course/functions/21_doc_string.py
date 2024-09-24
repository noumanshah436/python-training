"""
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition
Docstring is a short form of documentation string.
Its purpose is to give the programmer a brief knowledge about the functionality of the function.
It must be the first string  and it is also an optional string
To call a docstring we write the name of the function followed by ._doc_.

Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods,
but you should have a comment that describes what the method does.
This comment should appear after the def line. PEP 257 describes good docstring conventions.

"""


def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a + b) / 2
    # print(average)
    return average


v = function2(5, 7)
# print(v)
print(function2.__doc__)

sum((1, 2))

