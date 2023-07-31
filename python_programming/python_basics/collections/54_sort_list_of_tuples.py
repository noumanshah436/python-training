# ---------------------------------------
#  list of tuples

students = [("Squared", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krebs", "C", 78)]

# -----------------------------------------
# (sort by grade using proper function )


def grade_func(grades):  # takes a tuple(iterable) and return its specific index 1 value
    # print(grades)
    return grades[1]


"""
with key argument give a function object that takes a tuple(iterable)
 and return its specific index value ( to sort by that value)
"""
students.sort(key=grade_func)
# students.sort(key=grade_func, reverse=True)


# ----------------------------------------------

# (sort by grade using lambda func )
# work same as  above code


# grade = lambda grades: grades[1]       #  lambda function takes a tuple and return its index 1 value
# students.sort(key=grade)               # sorts current list
# students.sort(key=grade, reverse=True)

# ---------------------------------------------------------------
# (sort by age)

# age = lambda ages: ages[2]             # lambda function takes a tuple and return its index 2 value
# students.sort(key=age)
# students.sort(key=age, reverse=True)

# ---------------------------------------------------------------

print("\nusing for loop")
for i in students:
    print(i)

