def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


# calc factorial using recursion
print(fact(5))
