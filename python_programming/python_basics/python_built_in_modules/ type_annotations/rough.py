from typing import Annotated

def greet(name: Annotated[str, "The name of the person to greet"]) -> None:
    print(f"Hello, {name}!")

greet("Alice")