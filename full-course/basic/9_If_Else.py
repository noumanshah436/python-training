# if statement = a block of code that will execute if it's condition is true


# *************************
#
# age = int(input("How old are you?: "))
#
# if age >= 100:
#     print("You are a century old!")
# elif age >= 18:
#     print("You are an  adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# *************************
#
# list1 = [5, 7, 3]
# print(15 not in list1)
# if 15 not in list1:
#     print("No its not in the list")

# *********************************************

# shorthand if else: (used in case of single statement of both if else block )

# syntax:

# If-expression if(Condition) else else-expression

a = 5
b = 10
print("condition is True") if (a > b) else print("Condition is False")
# diff is that k bs if block ko if se pehle likh dia without using clon (:)

# ******

a = 330
b = 330

print("A") if a > b else (print("=") if a == b else print("B"))
