from collections import Counter

# collections.Counter can work with any iterable
# (list, tuple, string, dict keys, set, generator, etc.).

# Essentially, it just counts the frequency of hashable items (int, str, tuple, etc.)


# 1. List
years_list = ["2028", "2021", "2020", "2021", "2022"]
print("List:", Counter(years_list))

# 2. Tuple
years_tuple = ("2021", "2022", "2021", "2023")
print("Tuple:", Counter(years_tuple))

# 3. String (counts characters)
word = "banana"
print("String:", Counter(word))

# 4. Set (duplicates don’t exist, so counts will always be 1)
years_set = {"2021", "2022", "2023", "2021"}
print("Set:", Counter(years_set))

# 5. Dictionary (by default counts keys)
years_dict = {"2021": 10, "2022": 20, "2021": 15}  # duplicate keys overwrite
print("Dict Keys:", Counter(years_dict))

# To count values instead:
print("Dict Values:", Counter(years_dict.values()))

# 6. Generator / any iterable
gen = (x % 3 for x in range(10))  # values: 0,1,2,0,1,2...
print("Generator:", Counter(gen))
# Counter({0: 4, 1: 3, 2: 3})

# ---------------------------------

# when you use Counter with unhashable items like lists, dicts, or sets.

from collections import Counter

# Works fine with hashable items (int, str, tuple, etc.)
print("Hashable:", Counter([1, 2, 2, (3, 4), (3, 4)]))
# Counter({2: 2, (3, 4): 2, 1: 1})

# ❌ Fails with unhashable items (list, dict, set)
try:
    Counter([[1, 2], [1, 2], [3, 4]])  # list of lists
except TypeError as e:
    print("List inside Counter ->", e)

try:
    Counter([{"a": 1}, {"a": 1}, {"b": 2}])  # list of dicts
except TypeError as e:
    print("Dict inside Counter ->", e)

try:
    Counter([{1, 2}, {1, 2}, {3, 4}])  # list of sets
except TypeError as e:
    print("Set inside Counter ->", e)
