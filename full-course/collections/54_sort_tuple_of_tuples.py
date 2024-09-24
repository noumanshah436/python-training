
# tuple of tuples

students = (("Squared", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krebs", "C", 78))

#
# grade = lambda grades: grades[1]               # sort by grades
# sorted_students = sorted(students, key=grade)  # sorts and creates a new list


age = lambda ages: ages[2]         # sort by ages
sorted_students = sorted(students, key=age)  # sorts and creates a new list


for i in sorted_students:
    print(i)
