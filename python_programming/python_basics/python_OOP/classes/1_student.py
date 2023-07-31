# Chapter 38: Classes professionals notes (page 227)
#  D:\Python Notes

class Student:
    pass


harry = Student()
larry = Student()

harry.name = "Harry"    # instance variable of harry object
harry.std = 12
harry.section = 1

larry.std = 9           # instance variable of larry object
larry.subjects = ["hindi", "physics"]

print(harry.section, larry.subjects)
print(harry.__dict__)
print(larry.__dict__)

# **********************************

"""

The __dict__ attribute:
Every object in Python has an attribute which is denoted by __dict__, it maps
the all attribute names to their values. This dictionary is used to stores all the attributes
defined for the object itself. Following is the syntax of using __dict__:

object.__dict__

"""
