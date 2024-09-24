# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                creates a zip object with paired items of same index of each iterable
#                and  stored it in tuples for each item
# ============================================================
# The zip() function returns a zip object, which is an iterator of tuples
#   where the first item in each passed iterator(we give as argument) is paired together (in tuple) and
#   then the second item in each passed iterator are paired together (in another tuple) etc.

# If the passed iterators have different lengths, the iterator with the
# least items decides the length of the new iterator.
# ============================================================

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021", "1/2/2021", "1/3/2021"]

# --------------------------------------
# users = zip(usernames, passwords)   # by default it return a tuple of tuples
#
# users = list(zip(usernames, passwords))  # but we can cast it to any iterable
# # now it return a list of tuples
#
# print(type(users))      # list
# print(type(users[0]))   # tuple
#
# for i in users:
#     print(i)
#
# --------------------------------------
# users = dict(zip(usernames, passwords))
#
# for key, value in users.items():
#     print(key + " : " + value)

# # --------------------------------------
users = zip(usernames, passwords, login_dates)

for i in users:
    print(i)

# # --------------------------------
