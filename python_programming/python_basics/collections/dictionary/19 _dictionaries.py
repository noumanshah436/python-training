# dictionary =  A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly


d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])

# ***************************

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# capitals["Pakistan"] = "Islamabad"            # add to dictionary
# capitals.update({'Germany':'Berlin'})         # add key value to dic (same as above)
# capitals.update({'USA':'Las Vegas'})          # upadate value of a key
# capitals.pop('China')                         # remove a key value pair
# capitals.clear()

# print(capitals['Russia'])               # return value of the key i.e 'Moscow'
# print(capitals['Germany'])              # unsafe if key do not exist
# print(capitals.get('Germany'))          # safe if key do not exist
# print(capitals.keys( ))
# print(capitals.values())
# print(capitals.items())        # dict1.items() will return keys value pair as tuple

# capitals.items()  --- return list of tuples
# *******************


print(capitals.items())
# dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])
print(type(capitals.items()))
# <class 'dict_items'>

for key, value in capitals.items():
    print(key, ":", value)

for i in capitals.items():
    print(i, ":", type(i))


# *******************

# # iterate all keys
# print()
# for key,value in capitals.items():
#     print(key)

# *******************
# # iterate all values
# print()
# for key,value in capitals.items():
#     print(value)
