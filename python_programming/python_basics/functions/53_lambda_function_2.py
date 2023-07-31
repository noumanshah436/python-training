"""
 syntax 1 when we use inside a function ( it do not follow PEP8)

    lambda parameters : expression

 Example:
        double = lambda x: x * 2
        print(double(1))

********************************

syntax 2 when make an alias of lambda function ( follow PEP8)

     def aliasName(parameters): return expression

Example:
        def double(x): return x * 2
        print(double(1))

**************************************************

Always use a def statement instead of an assignment statement that binds
a lambda expression directly to a name.

use this:   def f(x): return 2*x

instead:    f = lambda x: 2*x

"""

# -------------------------------------

# def double(x):
#     return x*2

# def aliasName(parameters): return expression


def double(x): return x * 2


def multiply(x, y): return x * y


def add(x, y, z): return x + y + z


def full_name(first_name, last_name): return first_name+" "+last_name


def age_check(age): return True if age >= 18 else False


def practice(age): return True if age >= 18 else False


def check(age):                  # just using for testing
    return True if (age >= 18) else False


# ---------------------------

print(check(13))
print(double(2))
print(multiply(1, 2))
print(add(1, 2, 3))
print(full_name("Bro", "Code"))
print(age_check(18))

# -------------------------------------
