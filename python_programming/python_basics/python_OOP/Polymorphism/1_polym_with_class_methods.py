# Polymorphism with class methods:
# Below code shows how python can use two different class types, in the same way. We create a for loop
# that iterates through a tuple of objects. Then call the methods without being concerned about which class
# type each object is. We assume that these methods actually exist in each class.

# ********************
# Class Polymorphism in Python
# Polymorphism is a very important concept in Object-Oriented Programming.

# We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.

# We can then later generalize calling these methods by disregarding the object we are working with. Let's look at an example:


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

