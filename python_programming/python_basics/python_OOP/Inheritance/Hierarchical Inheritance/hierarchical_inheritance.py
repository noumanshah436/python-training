# Hierarchical Inheritance:
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

# If more than one class is inherited from the base class, it's known as hierarchical inheritance. In hierarchical inheritance, all features that are common in child classes are included in the base class.

# For example, Physics, Chemistry, Biology are derived from Science class.
# Similarly, Dog, Cat, Horse are derived from Animal class.


# Python program to demonstrate
# Hierarchical inheritance


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
