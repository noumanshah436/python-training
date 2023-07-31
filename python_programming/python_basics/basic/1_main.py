# variable = a container for a value. Behaves as the value that it contains
# *****************************************************

# string = a series of characters
first_name = "Bro"
last_name = "Code"
full_name = first_name + " " + last_name
print("Hello " + full_name)  # combine all pieces without space
print("Hello", ":", full_name)  # combine all pieces with a  space

# print(type(first_name))


# *****************************************************
# int = a whole integer

age = 21
age += 1
print("Your age is: " + str(age))
print(f"Your age is: {age}")
# print(type(age))
# *****************************************************

# float = a decimal number
height = 250.5
print("Your height is: " + str(height) + "cm")
# print(type(height))
# *****************************************************

# boolean = True or False
human = True
print("Are you a human: " + str(human))
# print(type(human))

x = 1j
print("complex " + str(x))
print(f"complex {type(x)} ,  {x}")
#

# *********************
x = range(6)
print("range " + str(x))
print(f"range {type(x)} ,  {x[0]}, {x[1]}, {x[5]} , {x}")

'''
*****************************************************
Python has the following data types built-in by default, in these categories:

Text Type:  	    str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:	    dict
Set Types:  	    set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview

*****************************************************

Setting the Data Type
In Python, the data type is set when you assign a value to a variable:

Example	                                        Data Type

x = "Hello World"	                              str
x = 20	                                        int
x = 20.5	                                      float
x = 1j	                                        complex
x = ["apple", "banana", "cherry"]	              list  (changeable)
x = ("apple", "banana", "cherry")	              tuple	(unchangeable)
x = range(6)	                                  range
x = {"name" : "John", "age" : 36}	              dict
x = {"apple", "banana", "cherry"}	              set
x = frozenset({"apple", "banana", "cherry"})	  frozenset
x = True	                                      bool
x = b"Hello"	                                  bytes
x = bytearray(5)                            	  bytearray
x = memoryview(bytes(5))                        memoryview

'''
