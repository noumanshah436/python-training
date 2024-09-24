# Python - property() function

# The property() function is used to define properties in the Python class.
#
# The property() method in Python provides an interface to instance attributes.
# It encapsulates instance attributes and provides a property, same as Java and C#.
#
# The property() method takes the get, set and delete methods as arguments and returns an object of the property class.
#
# It is recommended to use the property decorator instead of the property() method.
#
# property(fget, fset, fdel, doc)
#
# Parameters:
# fget: (Optional) Function for getting the attribute value. Default value is none.
# fset: (Optional) Function for setting the attribute value. Default value is none.
# fdel: (Optional) Function for deleting the attribute value. Default value is none.
# doc: (Optional) A string that contains the documentation. Default value is none.
#
# Return Value:
# Returns the property attribute from the given getter, setter, and deleter.
#


class person:
    def __init__(self):
        self.__name = ''
        # private instance attribute __name.

    def getname(self):
        print('getname() called')
        return self.__name

    def setname(self, name):
        print('setname() called')
        self.__name = name

    def delname(self):
        print('delname() called')
        del self.__name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(getname, setname, delname)

    # we can also set all separately as
    # name = property()
    # name = name.setter(setname)
    # name = name.getter(getname)
    # name = name.deleter(delname)


p1 = person()

p1.name = "Steve"
# setname() called

print(p1.name)
# getname() called
# 'Steve'

del p1.name
# delname() called


# In the above example, property(getname, setname, delname) returns the property object and assigns it to name.
# Thus, the name property hides the private instance attribute __name.
# The name property is accessed directly, but internally it will invoke the getname() or setname() method.


# As you can see above, the getname() method gets called automatically when we access the name property.
# In the same way, the setname method gets called when we assign a value to the name property.
# The delname() function would be invoked when you delete the name property.
