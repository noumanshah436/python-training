# For immutable objects (e.g., integers, strings, tuples):
#   A reference to the object is passed, not a copy.
#   Changes within the function result in the creation of a new object.


# For mutable objects(e.g., lists, dictionaries, sets):
#   A reference to the object is passed.
#   Changes within the function modify the same object, affecting it outside the function.


# This behavior illustrates Python's pass-by-object-reference mechanism.

# *******************************

def modify_immutable(x):
    print(f"Original id(x): {id(x)}")  # Prints the id of the passed object
    x += 1
    print(f"Modified id(x): {id(x)}")  # Prints the id of the new object
    print(f"Inside function: {x}")


a = 10
modify_immutable(a)
print(f"Outside function: {a}")
print(f"Original id(a): {id(a)}")  # id of `a` remains the same


# *******************************
def modify_mutable(lst):
    print(f"Original id(lst): {id(lst)}")  # Prints the id of the passed object
    lst.append(4)
    print(f"Inside function: {lst}")
    print(f"Modified id(lst): {id(lst)}")  # id remains the same


my_list = [1, 2, 3]
modify_mutable(my_list)
print(f"Outside function: {my_list}")
# id of `my_list` remains the same
print(f"Original id(my_list): {id(my_list)}")


# *******************************

var = [1, 2, 3, 4, 5]
print(type(var))
print(var)
print("memory address of var", id(var))  # 2381296172032


def myfunction1(v):
    print(v)
    print("memory Address of v", id(v))  # same address ( 2381296172032 )
    v[2] = 33
    print("print from function", v)
    print("Memory address of v", id(v))  # same address ( 2381296172032 )

    return v


myfunction1(var)
print(var)  # [1, 2, 33, 4, 5]
