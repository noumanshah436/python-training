"""
 closure =
            A function with preserved data.
            Give you access to an outer function’s scope,
            from an inner function.

            State of variables in outer scope are "saved".
            Variables in outer scope are considered "private".

     Main benefit of closure is that a closure retain the data or variables
        stored within

"""


# Python program to illustrate closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction


myFunction = outerFunction('Hey!')
myFunction()
