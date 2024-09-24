def hello():
    print("Hello")


print(hello)  # display the address of function in memory

hi = hello  # assign this address to a variable
print(type(hi))  # <class 'function'>

print(hi)  # same address as hello (treat hi as alias to hello)
hi()  # execute hello function


# ----------------------------

# make alias of print function

# say = print
# say("Whoa! I can't believe this works! :O")


# ----------------------------

def lost():
    print("lost function")


def work():
    print("work function")


lost = work
lost()  # now lost will call work function

# ----------------------------
