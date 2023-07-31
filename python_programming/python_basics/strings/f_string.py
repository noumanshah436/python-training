# 1 String Formatting (% Operator)
# 2 Using Tuple ()
# 3  String Formatting (str.format)
# 4 Using f-Strings ( f ):
import math

# **********************************

# 1 String Formatting (% Operator)
# same as printf in C ( we can also set width, precision and much more)

# name = "Nouman"
# var = 6
# n = "My name is %s." % name
# print(n)


# **********************************

# 2 Using Tuple ()
# The % operator takes only one argument, to mention more than one argument, use tuples

# name = "Nouman"
# var = 5
# s = " %s is in class %d" % (name, var)
# print(s)

# **********************************
# 3  String Formatting (str.format)

# var = "This article is written in {} ."
# print(var.format("Python"))

# **********************************

# 4 Using f-Strings ( f ):

# str1 = "Python"
# str2 = "Programming"
# print(f"Welcome to our {str1} {str2} tutorial")

# ***********

# F strings

# me = "Nouman"
# a1 = 3
#
# a = f"this is {me} {a1} {math.cos(65)}"
# a = f"this is {me} {a1} {56*6}"       # (we can also write expression within brackets)
#
# print(a)

# **********************************


