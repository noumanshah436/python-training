# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce((lambda x, y: x + y), letters)
print(word)   # HELLO

# working:
# take x=H and y=E   perform x+y=He
# now x=HE and y=L   perform x+y=HEl  and so on

# we do not have to  worry , how this reduce function do that,
# it just take a function that works on two arguments and give the desired result

# ===================================================

factorial = [5, 4, 3, 2, 1]
result = functools.reduce((lambda x, y: x * y), factorial )
print(result)
