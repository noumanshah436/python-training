class Employee:
    no_of_leaves = 8  # class variable
    pass


harry = Employee()
rohan = Employee()

harry.name = "Harry"  # instance variables of harry object
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"  # instance variables of rohan object
rohan.salary = 4554
rohan.role = "Student"

# ********

print(harry.__dict__)
harry.no_of_leaves = 10    # it will create new instance variable for harry  (class variable remain same)
print(harry.__dict__)

# ********

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9     # change value of class variable fr all objects
print(Employee.__dict__)
print(Employee.no_of_leaves)

"""

Instance variable:
"Instance variables are the variables for which the value of the variable is different for every instance."

Class variable:
"Class attributes are owned by the class directly, which means that they are not tied to any object or instance."
***************************************************************************************************************
Instance variables are created only for a specific object. The object can change, create, or update only its instance 
variables. While in the case of class variables, the variables and values we create or define are set as default 
for all the objects.
***************************************************************************************************************
The objects cannot change the value or variable in the class by just updating it using object_name.class_name.
When we try to change the value of class variable, it will create a new instance variable for the specific object,
that we are updating it for, hence defining the value to it.
***************************************************************************************************************
Objects can change the values of their particular instance variables. 
Making use of class and instance variables can ensure that our code adheres to the DRY (don't repeat yourself) 
principle to reduce repetition within code.

"""
