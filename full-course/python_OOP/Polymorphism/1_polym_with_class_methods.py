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


### Application of Class Polymorphism:

# 1. **Code Reusability**: Polymorphism allows you to reuse code by creating classes that implement the same interface but provide different implementations.

# 2. **Flexibility and Extensibility**: You can easily add new subclasses without modifying existing code, as long as they adhere to the interface specified by the superclass.

# 3. **Abstraction**: Polymorphism allows you to work with objects at a higher level of abstraction, focusing on what they can do rather than their specific implementations.

# In real-world applications, class polymorphism is used extensively in frameworks, libraries, and systems where
# flexibility and code reuse are important. For example, in GUI frameworks, different types of widgets (buttons, text
# fields, etc.) may all inherit from a common superclass and provide their own implementations for handling user
# interactions. Similarly, in web frameworks, different types of HTTP requests (GET, POST, etc.) may be treated
# uniformly, allowing developers to work with them using a common interface.
