# tuple =   collection which is ordered and unchangeable
#           used to group together related data

# for tuple of single element, we need an extra comma after element i.e. a=(1,)


# Tuples in Python :
a = ()    # It's an example of empty tuple
x = (1,)   # Tuple with single value i.e. 1
tup1 = (1, 2, 3, 4, 5)
tup1 = ('harry', 5, 'demo', 5.8)

# ********************************


student = ("Bro", "Bro", "male")

print(student[2])              # return item at specific index of tuple
print(student.count("Bro"))    # count of Bro in tuple (2)
print(student.index("male"))  # return index of element  (3)
print(student.__sizeof__())    # 56

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")

# ************

# To change value in tuple, first converted into list and then again in tuple
x = ("a", "b", "c")
y = list(x)
y [2] = "h"
x = tuple(y)

# ************

# Tuple Constructor in Python
# To create a tuple with a tuple constructor, we will pass the elements as its parameters.


tuple_constructor = tuple(("dsa", "developement", "deep learning"))
print(tuple_constructor)

# *****************

# Code for concatenating 2 tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')

# Concatenating above two
print(tuple1 + tuple2)
# (0, 1, 2, 3, 'python', 'geek')

# *************

# Nesting of Python Tuples
# A nested tuple in Python means a tuple inside another tuple.


# Code for creating nested tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')

tuple3 = (tuple1, tuple2)
print(tuple3)
# Output :

# ((0, 1, 2, 3), ('python', 'geek'))

# *************

#  Slicing in Tuples
# Slicing a Python tuple means dividing a tuple into small tuples using the indexing method.


# code to test slicing
tuple1 = (0 ,1, 2, 3)

print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
# Output:

# In this example, we sliced the tuple from index 1 to the last element. In the second print statement, we printed the tuple using reverse indexing. And in the third print statement, we printed the elements from index 2 to 4.

# (1, 2, 3)
# (3, 2, 1, 0)
# (2, 3)

# *************
