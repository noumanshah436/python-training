# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------

squares = []  # create an empty list
for i in range(1, 11):  # create a for loop
    squares.append(i * i)  # define what each loop iteration should do
print(squares)

# ----------
# now do same using list comprehension
# create a list AND defines what each loop iteration should do

squares = [i * i for i in range(1, 11)]
#                         It create a list and add items, whatever the expression(i*i) return on each iteration
print(squares)
print(type(squares))
print()
# --------------------------------------------------------------
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]


# add those students whose numbers are > = 60

# passed_students = list(filter(lambda x: x >= 60, students))  # using lambda function

passed_students = [i for i in students if i >= 60]           # only add those items which satisfy the condition
print(passed_students)

# --------------------------------------------------------------
# add those students whose numbers are > = 60 else save 'FAILED'


passed_students = [i if i >= 60 else "FAILED" for i in students]
#           add at some condition,  else add something different to list

print(passed_students)
