# https://www.geeksforgeeks.org/partial-functions-python/

# Partial functions allow us to fix a certain number of arguments of a function and generate a new function.

# Partial functions can be used to derive specialized functions from general functions and therefore help us to reuse our code.


from functools import partial

# A normal function
def f(a, b, c, x):
    return 1000*a + 100*b + 10*c + x

# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

# Calling g()
print(g(5))

# output:
# 3145

# ****************

# A normal function
def add(a, b, c):
    return 100 * a + 10 * b + c

# A partial function with b = 1 and c = 2
add_part = partial(add, c = 2, b = 1)

# Calling partial function
print(add_part(3))

# Output:
# 312

