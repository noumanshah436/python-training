var = [1, 2, 3, 4, 5]
print(type(var))
print(var)
print("memory address of var", id(var))  # 2381296172032


def myfunction1(v):
    print(v)
    print("memory Address of v", id(v))  # same address ( 2381296172032 )
    v[2] = 33
    print("print from function", v)
    print("Memory address of v", id(v))  # same address ( 2381296172032 )

    return v


myfunction1(var)
print(var)  # [1, 2, 33, 4, 5]
