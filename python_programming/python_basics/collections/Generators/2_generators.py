"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

# ********************************

def gen(n):
    for i in range(n):
        yield i


# g = gen(3)  # I can iterate it for 3 times (0 - 2) , 4th time cause error
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

# ********************************

# num = 546546
# str1 = "I am iterable"
# ier = iter(str1)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())

# for c in h:
#     print(c)

# ********************************


def factcal(n):
    if n==0 or n==1:
        return 1
    return n*factcal(n-1)

def factgen(n):
    i=1
    while i<=n:
        # print(f"fact {i}")
        yield factcal(i)
        i +=1

g = factgen(8)

for i in g:
    print(i)
