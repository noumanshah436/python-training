# ****************************************
# List comprehension

ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

ls = [i for i in range(100) if i%3==0]

print(ls)

# ****************************************
# dictionary comprehension


# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}

# dict2 = {key:value for key,value in dict1.items()}
# dict2 = {value:key for key,value in dict1.items()}   # reverse key and value in dic
# print(dict1,"\n", dict2)

# ****************************************
# set comprehension


# dresses = {dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]}
# print(type(dresses))

# ****************************************
# generator comprehension/expression


# evens = (i for i in range(100) if i % 2 == 0)
# print(evens.__next__())

# for item in evens:
#     print(item)

# ****************************************

# ask user for input items
# then ask with type of comprehension he want to use and do as he want

#
# no_of_list = int(input("How many items add in a list: "))
# input_string = input("Enter a list element separated by space ")
# lst = input_string.split()
# t = int(input("Which type of comprehension you use "
#               "1. List Comprehension "
#               "2.Dictionary Comprehension "
#               "3. Set Comprehension "))
# if t == 1:
#     ls = [i for i in lst]
#     print(ls)
#     print(type(ls))
# elif t == 2:
#     dict1 = {f'item{i}': i for i in lst}
#     print(dict1)
#     print(type(dict1))
# elif t == 3:
#     s = {i for i in lst}
#     print(s)
#     print(type(s))
