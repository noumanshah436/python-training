
# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0

# ******************************

# Working of for loop for Iterators

# The for loop in Python is used to iterate over a sequence of elements, such as a list, tuple, or string.

# When we use the for loop with an iterator, the loop will automatically iterate over the elements of the iterator until it is exhausted.


# create a list of integers
my_list = [1, 2, 3, 4, 5]

# create an iterator from the list
iterator = iter(my_list)

# iterate through the elements of the iterator
for element in iterator:
    # Print each element
    print(element)



# python3 ./Iterator/2_basics.py
