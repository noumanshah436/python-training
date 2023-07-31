# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# if we use walrus operator in place of a condition, it will always remain true.
# so if we use it in loop condition, we should break it inside that loop

# ------------------- 1 ----------------------

# happy = True
# print(happy)

# using walrus operator

# print(happy := True)

# -------------------- 2 ---------------------

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

# using walrus operator, we can write in more efficient way
# in less line lines of code

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)


# ------------------- 3 ----------------------

my_list = [1,2,3,4,5]
if len(my_list) > 3:
    print(f"The list is too long with {len(my_list)} elements")

# the walrus operator can eliminate calling the len() function twice as given below

my_list = [1,2,3,4,5]
if (n := len(my_list)) > 3:
    print(f"The list is too long with {n} elements")


# -----------------------------------------
