# list = used to store multiple items in a single variable
# A list is a data structure in Python that is a mutable, or
#   changeable, ordered sequence of elements.
# Each element or value that is inside of a list is called an item


# Lists in Python

lst = []  # list with no member, empty list
lst = [1, 2, 3]  # list of integers
lst = [1, 2.5, 3.7, 9]  # list of numbers (integers and floating point)
lst = ['a', 'b', 'c']  # list of characters
lst = ['a', 1, 'b', 3.5, 'zero']  # list of mixed value types
lst = ['One', 'Two', 'Three']  # list of strings
# *************************************************

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
#
# print(food[0])
# print(food[3])
# print(food[3][4])   # print 4th letter of index 3 value


# food[0] = "sushi"   # update/change list value

# food.append("ice cream")       # add value at last
# food.remove("hotdog")
# food.pop()                     # remove last element
# food.insert(0,"cake")          # insert at specific index i.e (index , value)
# food.sort()                    # sort alphabetically
# food.clear()                   # remove all items in list

# print("length of list:", len(food))
# for x in food:
#     print(x)

# *********************************************************
#  Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract
# the values into variables. This is called unpacking.
# *********************************************************

# fruits = ["apple", "banana", "cherry", 1]
# x, y, z, a = fruits
# print(x, type(x))
# print(y)
# print(z)
# print(a, type(a))

# *********************************************************
# Input from user until it give one of the value in the list
# *********************************************************
choices = ["rock", "paper", "scissors"]
player = None
while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

print(player)
