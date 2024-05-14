# https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/

#  In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. 
# In Python, we can actually change the behavior of code at run-time.

# Monkey patching is a technique used in Python to modify or extend the behavior of a module or class at runtime.
# It involves dynamically changing or replacing attributes or methods of an object.

import monk 

# Example 1

# Define our new implementation of greeting
def new_greeting():
    return "Hey there!"

# Monkey patching: replace the original greeting function with our new implementation
monk.greeting = new_greeting

# Now when we call greeting(), it will return the new message
print(monk.greeting())  # Output: Hey there!

# *********************************
# Example 2

def monkey_f(self): 
     print ("monkey_f() is being called") 
   
# replacing address of "func" with "monkey_f" 
monk.A.func = monkey_f 


obj = monk.A() 
  
# calling function "func" whose address got replaced 
# with function "monkey_f()" 
obj.func() 
