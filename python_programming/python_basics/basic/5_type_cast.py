# type casting = convert the data type of a value to another data type.

# Implicit Type Conversion is automatically performed by the Python interpreter.
# Python avoids the loss of data in Implicit Type Conversion.

# Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
# In Type Casting, loss of data may occur as we enforce the object to a specific data type.

x = 1       # int
y = 2.0     # float
z = "3"     # str

# Explicit Type Conversion

x = int(x)
y = int(y)
z = int(z)

x = float(x)
y = float(y)
z = float(z)

x = str(x)
y = str(y)
z = str(z)

print(x)
print(y)
print(z * 3)

# *******************

#  Implicit Type Conversion
#  Python always converts smaller data types to larger data types to avoid the loss of data.

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

# Output

# Value: 124.23
# Data Type: <class 'float'>
