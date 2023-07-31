# sort() method   = only used with lists         (builtin method for lists)
# sorted() function = used with any iterable     (i.e lists , tuples , dictionaries etcc.)

# ----------------------------------------
#  sort lists  using sort() method

students = ["Squared", "Sandy", "Patrick", "Spongebob", "Mr.Krebs", "Zubair", "Ahmad"]
students.sort()
# students.sort(reverse=True)     # keyword argument to sort in reverse order


for i in students:
    print(i)


# ---------------------------------------
# sort iterables  using sorted() function
#
# students = ("Melina", "Sandy", "Patrick", "Spongebob", "Mr.Krebs")   # tuple (iterables)
# sorted_students = sorted(students)          # takes an iterable and create & returns a sorted list
#
# for i in sorted_students:
#     print(i)

# ------------------------------------
