# function = a block of code which is executed only when it is called.
# **********************************************


def hello (first_name, last_name, age):
    print("hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")


hello("Bro", "Code", 21)

# **********************************************


def check_age(age):
    return True if (age >= 18) else False


# return true if age is greater than or equal to 18 else return false
check_age(12)


