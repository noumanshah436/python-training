# Python Generator Expression

# Simple generators can be easily created on the fly using generator expressions. It makes building
# generators easy.
#
# Similar to the lambda functions which create anonymous functions, generator expressions create
# anonymous generator functions.
#
# The syntax for generator expression is similar to that of a list comprehension in Python.
# But the square brackets are replaced with round parentheses.
#
# The major difference between a list comprehension and a generator expression is that a list
# comprehension produces the entire list while the generator expression produces one item at a time.
#
# They have lazy execution ( producing items only when asked for ). For this reason, a generator
# expression is much more memory efficient than an equivalent list comprehension.

#
# ********************************************

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)

print(list_)
print(generator)

# The generator expression did not produce the required result immediately. Instead, it returned a
# generator object, which produces items only on demand.

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator))
