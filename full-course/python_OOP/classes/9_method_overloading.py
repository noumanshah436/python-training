# Method Overloading, a way to create multiple methods with the same name but different arguments, is not possible in Python.

# Method overloading occurs when a class contains many methods with the same name.
#   The types and amount of arguments passed by these overloaded methods vary.

# Python does not support method overloading or compile-time polymorphism.
# If there are multiple methods with the same name in a class or Python script, the method specified in the latter one will override the earlier one.

# ************************

# why not method overloading:
# Python does not use function arguments in method signatures, hence method overloading is not supported.

# Python, there is no concept of method overloading based on function arguments because
#  Python's functions do not include type information in their signatures
#   (i.e. you don't need to specify the types of the function's parameters in its signature)

#  Unlike some statically-typed languages like C++ or Java, where you must explicitly declare the data types of function arguments,
# Python is dynamically-typed, meaning that the type of an object is determined at runtime.
