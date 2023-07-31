list1 = [["Harry", 50], ["Larry", 45],
         ["Carry", 30], ["Marie", 38]]

for i in list1:  # i will iterate  through list (single items inside list)
    print(i)

# list unpack
for name, grade in list1:  # name will have first element of list and grade have second
    print(name, grade)

# *********************

dict1 = dict(list1)  # now we have dictionary

for item in dict1:  # only get keys in dictionary
    print(item)

for item in dict1.items():  # dict1.items() will return keys value pair as tuple
    # print(type(item))
    print(item)

# unpack dictionary
for name, grade in dict1.items():
    print(name, " achieve ", grade)

# *********************

# only get numbers > 6 from list of mix values

# items = [int, float, "Nomi", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]
#
# for item in items:
#     if str(item).isnumeric() and item >= 6:
#         print(item)


# *********************

lst = "BSCSF18M001,Ali,5,3.5".split(",")
print(lst)
dic = {"Roll num": lst[0], "name": lst[1], "Sem": lst[2], "CGPA": lst[3]}
# print(dic)

list = [str(dic[x]) for x in dic.keys()]
string = ','.join(list)
print(string)
