# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/


# A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original(child objects).

# Syntax of Shallow copy
# Syntax: copy.copy(x)

# *******************************

#  A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original (child).

# Syntax of Deep copy
# Syntax: copy.deepcopy(x)

# ****************************


# # copy using = operator
# list1 = [1, 2, 3, 4]
# list2 = list1
#
# print("list1:", list1, id(list1))
# print("list2:", list2, id(list2))
#
# list1.append(34)
# print("list1:", list1, id(list1))
# print("list2:", list2, id(list2))


#  ******************

# # creating a copy using shallow copy
#
# print("creating a copy using shallow copy")
# import copy
#
# old_list = [1, 2, 3, 4, [10, 20]]
# new_list = copy.copy(old_list)
# # new_list will have the reference of old_list items
#
# print("old_list:", old_list, id(old_list))
# print("new_list:", new_list, id(new_list))
#
# old_list.append(55)
# print("old_list:", old_list, id(old_list))
# print("new_list:", new_list, id(new_list))
#
# old_list[4][1] = 23  # this will update at both list
# print("old_list:", old_list, id(old_list))
# print("new_list:", new_list, id(new_list))
#


import copy
print("creating a copy using deep copy")


old_list = [1, 2, 3, 4, [10, 20]]
new_list = copy.deepcopy(old_list)
# deep copy will create a new duplicate object for the new_list
# and recursively add the copies of old object in new object

print("old_list:", old_list, id(old_list))
print("new_list:", new_list, id(new_list))

old_list.append(55)
print("old_list:", old_list, id(old_list))
print("new_list:", new_list, id(new_list))

old_list[4][1] = 23  # this will only update old_list
print("old_list:", old_list, id(old_list))
print("new_list:", new_list, id(new_list))
