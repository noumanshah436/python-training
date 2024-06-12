def myFunc(age):
    print(id(age))
    age = age + 10
    print(id(age))


var = 21
print(id(var))
myFunc(var)

# ***********************

print(id(5))
a = 5
b = 5
print(id(a))
print(id(b))

# ************************


list1 = [1, 2, 3]

# list2 = list1   # do not make copy (both point to same list)
list2 = list(list1)   # makes another copy and return it

list2[0] = 444
print(list1, list2, sep="\n")

print(id(list1), id(list2))

# ************************
