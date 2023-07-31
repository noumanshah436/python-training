# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

# map takes a function that takes an item ( single item in the iterable )
# and return it by modifying as we want

# map function return a map object that can be cast to any iterable

# ---------------------------------

#         ( item, price)
store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]


#   make lambda function that takes a tuple and return this tuple
#     by modifying its price value

to_euros = lambda data: (data[0], data[1]*0.82)       # consider price is in dollar in sore
# to_dollars = lambda data: (data[0],data[1]/0.82)    # consider price is in euros in sore

store_euros = list(map(to_euros, store))


print(type(store_euros))    # list
print(type(store_euros[0]))   # tuple

for i in store_euros:
    print(i)

# -----------------------------------

# practice map

# add 10 to each item in the iterable (grade list)

grades = [50, 40, 60, 80, 90]

# function that takes an int (single item in list) and return by adding 10
add_10 = lambda grade: grade+10

new_grades  = list(map(add_10, grades))

for i in new_grades:
    print(i)


