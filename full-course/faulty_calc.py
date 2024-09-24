def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b

#
# opr1 = [45, 56, 56]
# opr2 = [3, 9, 6]
# op = [3, 1, 4]
#
#
# def fault(a, b):
#     if ((a in opr1) and (b in opr2)):
#         return 12
#
#
# fault(45,3)

def calculator():
    value1 = int(input("enter 1st operands:"))
    value2 = int(input("enter 1st operands:"))
    print("Enter Operation Number:\n"
          "1. Addition\n" +
          "2. sub\n" +
          "3. mul\n" +
          "4. divide")
    op = int(input(":"))
    # print(value1,value2,op)

    if op == 1:
        print(add(value1, value2))
    elif op == 2:
        print(sub(value1, value2))
    elif op == 3:
        print(mul(value1, value2))
    elif op == 4:
        print(div(value1, value2))

calculator()
