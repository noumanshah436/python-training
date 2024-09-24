"""
Join is a function in Python, that returns a string by joining the elements
of an iterable, using a string or character of our choice.

In the case of join function, the iterable can be a list, dictionary, set, tuple,
or even a string itself. The string that separates the iterations could be anything.
It could just be a comma or a full-length string. We can even use a blank space
or newline character (/n ) instead of a string.

"""


lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

# without join method:
# for item in lis:
#     print(item, "and", end=" ")


# a = ", ".join(lis)
# print(a, "other wwe superstars")

# a = " and ".join(lis)
# print(a, "other wwe superstars")


# **********************************

# limitations to join() function

# 1)  For join function, all the variables should have the
#     same sort of data type, either it is an integer, string, or any other,
#     otherwise the join function will not work and cause error
# 2) In the case of the dictionary, the join function will only return the key part,
#      separated by the string in between,leaving the value side behind.

# *********

# 1)
# input_list = ["Test1", 13, "Test2", 24, "Test3", 100, "Test4"]
# sep = '_'
# out = sep.join(input_list)  # cause error
# print(out)

# **********

# 2)
# myDictionary = {"name": "Jack", "country": "America"}
# separator = "_separator_"
# print(separator.join(myDictionary))


