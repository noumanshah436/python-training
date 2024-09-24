
# https://www.youtube.com/watch?v=Wbd8W2zW-aI
# https://sbcode.net/python/command/

# The Command Design Pattern in Python
# The command pattern is a behavioural design pattern,
# in which an abstraction exists between an object that invokes a command, and the object that performs it.

# The components if the Command Design Pattern are,
    # The Receiver - The Object that will receive and execute the command
    # The Invoker - Which will send the command to the receiver
    # The Command Object - Itself, which implements an execute, or action method,
    # and contains all required information or module which is aware of
    # the Receiver, Invoker and Commands

# Eg, a button, will call the Invoker, which will call a pre registered Commands execute method,
# which will perform the action on the Receiver.

# Notes:
# The receiver object should manages it's own state, not the command object
# There can be one or more invokers which can execute the command at a later date.

# pylint: disable=arguments-differ
"The Command Pattern Concept"
from abc import ABC, abstractmethod

class ICommand(ABC):
    "The command interface, that all commands will implement"
    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"

class Invoker:
    "The Invoker Class"

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command

    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")

class Receiver:
    "The Receiver"

    @staticmethod
    def run_command_1():
        "A set of instructions to run"
        print("Executing Command 1")

    @staticmethod
    def run_command_2():
        "A set of instructions to run"
        print("Executing Command 2")

class Command1(ICommand):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()

class Command2(ICommand):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()

# The CLient
# Create a receiver
RECEIVER = Receiver()

# Create Commands
COMMAND1 = Command1(RECEIVER)
COMMAND2 = Command2(RECEIVER)

# Register the commands with the invoker
INVOKER = Invoker()
INVOKER.register("1", COMMAND1)
INVOKER.register("2", COMMAND2)

# Execute the commands that are registered on the Invoker
INVOKER.execute("1")
INVOKER.execute("2")
INVOKER.execute("1")
INVOKER.execute("2")
