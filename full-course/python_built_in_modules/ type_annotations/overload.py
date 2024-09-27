# The `@overload` decorator allows you to define multiple function signatures for a single function.
#
# This is particularly useful when a function can accept different types of inputs and return
#    different types of outputs depending on the input type.

# The `@overload` decorator helps static type checkers (like `mypy`) understand the different possible function signatures, though it doesn't actually implement different behaviors at runtime.

# Here’s an example of how to use `@overload`:

# Example with `@overload`

from typing import overload, Union, List


@overload
def process(value: int) -> int:
    # this is just to helps type checker that if input value is int then return value will be int
    ...


@overload
def process(value: str) -> str:
    # this is just to helps type checker that if input value is str then return value will be str
    ...


def process(value: Union[int, str]) -> Union[int, str]:
    if isinstance(value, int):
        return value * 2  # For int, multiply by 2
    elif isinstance(value, str):
        return value.upper()  # For str, return uppercase
    raise TypeError("Invalid type")

# Explanation:
# - **Overloads**: You define multiple `@overload` signatures above the actual implementation. These are type hints that specify the function's behavior for different types of input.
# - **Implementation**: The actual function only contains the logic that handles different types. Static type checkers will refer to the overloads, but the runtime will only use the actual function.

# Use Case:


result1 = process(5)        # Returns 10, the int overload applies
result2 = process("hello")  # Returns "HELLO", the str overload applies

# Key Points:
# - **@overload does not provide the function implementation**: The overloaded signatures are purely for type hinting purposes. You must provide a single implementation that handles the various input types.
# - **Static type checking only**: The overloaded signatures help tools like `mypy` infer the correct types when checking code but do not affect runtime behavior.

# ********************************************

# Example with `@overload` in Class Context

# The `@overload` decorator can also be used in methods or constructors of classes:


class Box:
    @overload
    def add(self, item: int) -> None:
        ...

    @overload
    def add(self, item: List[int]) -> None:
        ...

    def add(self, item):
        if isinstance(item, int):
            print(f"Added single item: {item}")
        elif isinstance(item, list):
            print(f"Added list of items: {item}")

# Here, both signatures of `add` are valid, but they lead to the same implementation.
