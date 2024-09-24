# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))

d2 = {"Harry": "Burger",
      "Rohan": "Fish",
      "SkillF": "Roti",
      "Shubham": {"B":"maggie", "L":"roti", "D":"Chicken"}}

#
# d2["Ankit"] = "Junk Food"      # add to dictionary
# d2[420] = "Kebabs"             # key can be of any type
# print(d2)
# del d2[420]                # delete an item

# print(d2["Shubham"])
# print(d2["Shubham"]["B"])


# d3 = d2   # d3 points to same dic, any change in one, reflect to both
# d3 = d2.copy()  # now d3 have its own copy, both are separate
# d3["h"] = "hello"
# del d3["Harry"]
# print(d2)
# print(d3)

# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(d2.items())


# *********************

# Dictionary keys must be immutable, such as tuples, strings, integers, etc.
# We cannot use mutable (changeable) objects such as lists as keys.

# Valid dictionary

my_dict = {
  1: "Hello",
  (1, 2): "Hello Hi",
  3: [1, 2, 3]
}

print(my_dict[(1,2)])
# 'Hello Hi'
