# Type annotations
#     specify type hints that helps programmers to know, what should be the type for a given object
# *******************

# for non-class variables
name: str = "Nouman"
print(name)

# *******************

# specify return type:


def check_access1() -> str:
    print("check_access1")
    return "hello"


check_access1()

# *******


def check_access2() -> bool:
    print("check_access2.")
    return True


check_access2()


# *****


def check_access3() -> None:
    print("check_access3.")


check_access3()

# **************************************

# specify argument type and return type both


def make_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


print(make_full_name("Syed", "Nouman"))

# ***********


def add(x: int, y: int) -> int:
    return x + y


print(add(5, 10))
