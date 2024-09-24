# The with statement itself ensures proper acquisition and release of resources.

try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")

# *******************

# open will return file handler or file pointer

# f = open("C:\\Users\\Nouman\\Desktop\\test.txt", "rt")
f = open("/home/dev/Desktop/test.txt", "rt")

# ***************************
# content = f.read()         #  read complete file and store as string

# content = f.read(3)          # read next 3 characters
# content = f.read(34455)      # read next 34455 characters as string

# print(type(content))      # <class 'str'>
# print(type(f))            # <class '_io.TextIOWrapper'>
# print(content)

# ***************************

# for i in content:       # iterate through file char by char
#     print(i)

# ***************************

# for i in f:              # iterate through file line by line
#     print(i, end="")

# ***************************

# read next line with new line character at the end of that line
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")

# ****************************

# makes a list of lines of the complete file ( start from the location of pointer f)
# print(f.readlines())

# ****************************


f.close()
