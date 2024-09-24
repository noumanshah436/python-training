# The enumerate() function assigns an index to each item in an
#   iterable object that can be used to reference the item later.

# enumerate() combine index and item in a tuple

# syntax
# enumerate(iterable)
# enumerate(iterable , start = 0 )

# by default start assigning from 0
# We can loop through string, tuple or objects using enumerate


# *********************************

l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# for index, item in enumerate(l1, start=5):
#     if index == 6:
#         continue
#     print(index, ":", item)

# ********************************

cars = ['kia', 'audi', 'bmw']

# for car in enumerate(cars):     # use as item as tuple
#   print(car)

# for index, item in enumerate(cars):   # split tuple into index and item
#     print(index, item)


# ********************************

# lst = []
# cars = ['kia', 'audi', 'bmw']
# for car in enumerate(cars):
#     print(type(car), car)
#     lst.append(car)
#
# print(lst)

# ********************************

# if we do not use enumerate
# cars = ['kia', 'audi', 'bmw']
# listOfCars = []
# n = 0
# for car in cars:
#     listOfCars.append((n, car))  # append a  tuple
#     n += 1
# print(listOfCars)

# above code can be simplified using enumerate as
# cars = ['kia', 'audi', 'bmw']
# print(list(enumerate(cars)))

# ********************************
#
# str1 = "HelloWorld"
# print(list(enumerate(str1)))
# print(id(str1))
# print(str1)
#
# print(enumerate(str1))

# ********************************

# cars = ('kia', 'audi', 'bmw')
# for index, car in enumerate(cars):
#     print(car)
