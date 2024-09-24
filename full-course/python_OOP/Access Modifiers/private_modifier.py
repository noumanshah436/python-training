# Private Access Modifier:
# The members of a class that are declared private are accessible within the class only,
# private access modifier is the most secure access modifier. Data members of a class are declared
# private by adding a double underscore ‘__’ symbol before the data member of that class.

# we can access private members using name mangling as obj._class__privateMember outside of class


# program to illustrate private access modifier in a class

class Geek:
    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __display_details(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)
        print("end function")

    # public member function
    def access_private_function(self):
        # accesing private member function
        self.__display_details()


# creating object
obj = Geek("R2J", 1706256, "Information Technology")

print(obj._Geek__name)
print(obj._Geek__display_details())

# calling public member function of the class
obj.access_private_function()
