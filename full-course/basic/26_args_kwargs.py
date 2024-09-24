"""
*args =   parameter that will pack all arguments into a tuple (unchangeable)
          useful so that a function can accept a varying amount of arguments  """


# using args as name is convention , we can use any name instead

def add(*args):
    total = 0
    print("type(args):", type(args))  # <class 'tuple'>
    print("args:", args)  # (1, 2, 3, 4)
    print("*args:", *args)  # 1 2 3 4
    print("args[0]:", args[0])  # it works , but it can be risky as it can cause IndexError: tuple index out of range

    for i in args:
        total += i
    return total


def change_first_value_of_received_arguments(*args):
    total = 0
    stuff = list(args)  # convert tuple to list so it can be changeable
    stuff[0] = 0
    for i in stuff:
        total += i
    return total


print(add(1, 2, 3, 4))

# ********************************

"""
**kwargs =   parameter that will pack all arguments into a dictionary
             useful so that a function can accept a varying amount of keyword arguments  """


def hello(**kwargs):
    print(kwargs)
    # {'title': 'Mr.', 'first': 'Syed', 'middle': 'Nouman', 'last': 'Ab. Rehman', 'age': 23}
    print("Hello " + " " + kwargs['title'] + " " + kwargs['middle'] + kwargs['first'] + " " + kwargs['last'])

    print("Type ", type(kwargs['age']))  # <class 'int'>

    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Syed", middle="Nouman", last="Ab. Rehman", age=23)

# *********************

print("end")
a = (1, 2, 3, 4)
print(*a)
