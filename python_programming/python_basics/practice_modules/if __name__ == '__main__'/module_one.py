# ***********************************
# if __name__ == '__main__'
# ***********************************
# 1. Module(python file) can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules
# -------------------------
# note: when we import a module, it will run it's module code first
# -------------------------
# BY including the above statement we can check that if the module
#    is running directly(run itself) or indirectly(run by other module)
# -------------------------
#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#      the initial module being run

# ==================================================

# check assigned value of __name__

# import module_two
# print(__name__)             # if we run module in itself, its __name__ variable will contain  '__main__'
# print(module_two.__name__)  # if we import a module , its __name__ variable will contain the name of its module

# -----------------------------------------

# check module is running directly or indirectly

# if __name__ == '__main__':
#     print("running module_one directly")
# else:
#     print("running module_one from other module indirectly")


# -----------------------------------------
x = 10


def hello():
    print("hello :", x)


# -------------------------------
# call to a main function

def main():
    print("Hello!")


if __name__ == '__main__':
    main()
