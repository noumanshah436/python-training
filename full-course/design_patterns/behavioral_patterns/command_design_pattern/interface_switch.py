"The switch interface, that all commands will implement"
from abc import ABC, abstractmethod

class ISwitch(ABC):
    "The switch interface, that all commands will implement"

    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"
