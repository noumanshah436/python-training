# pop syntax:
# value = my_dict.pop(key[, default])

# key: The key of the item to be removed from the dictionary.
# default (optional): If provided, this value is returned if the key is not found in the dictionary.


my_dict = {'a': 1, 'b': 2, 'c': 3}

value = my_dict.pop('b')
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

# Providing a default value for a non-existing key
value = my_dict.pop('d', 0)
print(value)  # Output: 0


# **********************

# popitem():
# The popitem() method removes and returns an arbitrary key-value pair from the dictionary.
# Since dictionaries are unordered before Python 3.7 and insertion-ordered from Python 3.7,
# the key-value pair that is popped is not guaranteed to be any specific item.
# In Python 3.7 and later versions, popitem() removes the last inserted item.

# Syntax:
# key, value = my_dict.popitem()

my_dict = {'a': 1, 'b': 2, 'c': 3}

key, value = my_dict.popitem()
print(key, value)  # Output (varies): e.g., ('a', 1)

print(my_dict)  # Output (varies): {'b': 2, 'c': 3}

# **********************


# In summary, pop() is used when you want to remove a specific item from the dictionary based on its key,
# while popitem() is used when you want to remove and return an arbitrary key-value pair from the dictionary,
# which is particularly useful when you don't care about the order of removal.
