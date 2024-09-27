from typing import Sequence, TypeVar

T = TypeVar("T")

def first(values: list[T], default: T) -> T:
    if len(values) == 0:
        return default
    return values[0]

names = ["Harry", "Barry", "Warry"] # list[str]
first_name = first(names, "") # str


numbers = [1, 2, 3, 4]
first_number = first(numbers, 0) # int

# T will be used as a placehoslder for our type