capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'Pakistan': 'Islamabad',
            'China': 'Beijing',
            'Russia': 'Moscow'}

user_input = input("input Country to get its capital : ")
# ans = capitals.get(user_input)

if user_input in capitals:
    print(capitals.get(user_input))
else:
    print("Not found")

# print(type(capitals.items()))
# print(type(capitals))

# ********************************

d = {}
key = "nomi"
value = "1998"
d[key] = value
print(d)
