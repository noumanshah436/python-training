
# we can directly import module from package

# from functions import arithmetic 
# print(arithmetic.add(2, 4))

# **********************

"""
if I import package "function"(my own package) 
it will automatically excute __init__.py file in this package
so we can do our initial stuff in it

for example:  
    i) initialize our object in it like flask object 
    ii) import other modules in __init__.py file ,
        so we don't need to explicitly import them
"""

#   use of  __init__.py file

# from functions.arithmetic import add         # here we explicitly import arithmetic module
from functions import add    

print(add(12, 4))


# import os
# print(os.path)

# python main.py