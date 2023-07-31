# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

print("1The " + animal + " jumped over the " + item)

# {} = format-field  or Place-Holder
print("2The {} jumped over the {}".format("cow", "moon"))
print("3The {} jumped over the {}".format(animal, item))
print("4The {1} jumped over the {0}".format(animal, item))  # positional arguments
print("5The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword arguments

text = "The {} jumped over the {}"
print(text.format("cow", "moon"))

print()
# ***********************************************

name = "Bro"

print("My name is {}".format(name))
print("My name is {:10}. Nice".format(name, name))  # amount of padding
print("My name is {:<10}. Nice".format(name, name))  # < = left align  ( default )
print("My name is {:>10}. Nice".format(name, name))  # > = right align
print("My name is {:^10}. Nice".format(name, name))  # ^ = center align

# with positional or keyword arguments  = {argument:padding}
print("The {1:10} jumped over the {0:10}".format(animal, item))  # positional arguments
print("The {animal:10} jumped over the {item:10}".format(animal="cow", item="moon"))  # keyword arguments
print()


# ***********************************************

number = 1000

print("The number pi is {:.3f}".format(number))  # display 3 digits after decimal point
print("The number pi is.{:<10.3f} end".format(number))  # display 3 digits after decimal with width = 10 align it left
print("The number is {:,}".format(number))  # add comma to 1000 places
print("The number is {:b}".format(number))  # binary representation of number
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))  # hexadecimal representation of number with all upper case
print("The number is {:x}".format(number))  # hexadecimal representation of number with all lower case

print("The number is {:E}".format(number))  # scientic notation representation of number with upper case E
print("The number is {:e}".format(number))  # scientic notation representation of number with lower case e


# ***********************************************
# f-strings

str1 = "Python"
str2 = "Programming"
print(f"Welcome to our {str1} {str2} tutorial")
print()
