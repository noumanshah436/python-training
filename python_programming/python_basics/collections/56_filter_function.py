# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Ali",19),
           ("Afridi",18),
           ("Rizwan",17),
           ("Ahmad",16),
           ("Naveed",21),
           ("Waleed",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)