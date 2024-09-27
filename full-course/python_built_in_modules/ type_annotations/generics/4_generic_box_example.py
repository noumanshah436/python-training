
# https://www.youtube.com/watch?v=ChRDzldOz8g

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Apple:
    name: str = 'Apple'


@dataclass
class Banana:
    name: str = 'Banana'


class Box(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def remove(self, item: T) -> None:
        self.items.remove(item)


class BananaBox(Box[Banana]):
    # we are setting the generic type to Banana, the type T is always Banana
    pass


apple_box = Box[Apple]()
apple_box.add(Apple())
# apple_box.add(Banana()) # error: Argument 1 to "add" of "Box" has incompatible type "Banana"; expected "Apple"  [arg-type]


banana_box = BananaBox()
banana_box.add(Banana())
# Type error: eArgument 1 to "add" of "Box" has incompatible type "Apple"; expected "Banana"  [arg-type]
banana_box.add(Apple())
