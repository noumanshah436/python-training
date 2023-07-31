
# Use lambda functions when an anonymous function is required for a short period of time.
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument
#      will be multiplied with an unknown number:

# Use that function definition to make a function that always doubles/triple the number you send in:


def my_func(n):
    return lambda a: a * n
    # return lambda function


my_double = my_func(2)    # remember lambda is also a function and we can make its alias
my_triple = my_func(3)

print(my_double(11))   # output 22
print(my_triple(11))   # output 33

"""
consider my_double as

def my_double(a):
    return a*2

"""
