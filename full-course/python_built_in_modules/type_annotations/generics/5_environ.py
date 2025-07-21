import os
from typing import Callable, Generic, TypeVar, cast, overload

T = TypeVar("T")
C = TypeVar("C")

src = {
    "FOO": "1",
    "BAR": "2",
    "BAZ": "3",
}


class EnvVar(Generic[T]):

    @overload
    def __init__(self: "EnvVar[str | None]", name: str) -> None:
        # this is just to helps type checker that if only name(str) is given then
        # this instanec will be of type EnvVar[str | None], menas T will be str or None
        ...

    @overload
    def __init__(self: "EnvVar[str]", name: str, *, default: str) -> None:
        # this is just to helps type checker that if name(str) and defaul(strt is given then
        # this instanec will be of type EnvVar[str] menas T will be str
        ...

    @overload
    def __init__(
        self: "EnvVar[C]",
        name: str,
        *,
        default: str | None = None,
        converter: Callable[[str | None], C] | None = None,
    ) -> None:
        ...

    def __init__(
        self,
        name: str,
        *,
        default: str | None = None,
        converter: Callable[[str | None], C] | None = None,
    ) -> None:
        self.name = name
        self.default = default
        self.converter = converter

    @property
    def value(self) -> T:
        value = src.get(self.name, self.default)

        if self.converter:
            return cast(T, self.converter(value))

        return cast(T, value)


def as_int(value: str | None) -> int:
    return int(value) if value else 0


EnvVar("FOO").value
EnvVar("FOO", default="1").value
EnvVar("FOO", converter=as_int).value
EnvVar("FOO", converter=bool).value
