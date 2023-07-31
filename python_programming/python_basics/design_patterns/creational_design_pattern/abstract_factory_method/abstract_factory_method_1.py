# Abstract Factory is a creational design pattern, which solves the problem of creating entire product families without specifying their concrete classes.

# Abstract Factory is a design pattern used to create families of related objects without specifying their concrete classes.
# It provides an interface for creating objects, but the actual implementation of the objects is deferred to concrete factory classes.
# This pattern helps achieve the goal of creating objects with a consistent and cohesive theme.

import abc

# Abstract Factory
class GUIFactory(abc.ABC):
    @abc.abstractmethod
    def create_button(self):
        pass

    @abc.abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factory for Windows
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Concrete Factory for macOS
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# Abstract Product: Button
class Button(abc.ABC):
    @abc.abstractmethod
    def render(self):
        pass

# Concrete Product for Windows
class WindowsButton(Button):
    def render(self):
        return "Render a Windows style button"

# Concrete Product for macOS
class MacOSButton(Button):
    def render(self):
        return "Render a macOS style button"

# Abstract Product: Checkbox
class Checkbox(abc.ABC):
    @abc.abstractmethod
    def render(self):
        pass

# Concrete Product for Windows
class WindowsCheckbox(Checkbox):
    def render(self):
        return "Render a Windows style checkbox"

# Concrete Product for macOS
class MacOSCheckbox(Checkbox):
    def render(self):
        return "Render a macOS style checkbox"

# Client code
def create_gui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    return button, checkbox

if __name__ == "__main__":
    # Create a Windows GUI
    windows_factory = WindowsFactory()
    windows_button, windows_checkbox = create_gui(windows_factory)
    print(windows_button.render())  # Output: Render a Windows style button
    print(windows_checkbox.render())  # Output: Render a Windows style checkbox

    # Create a macOS GUI
    macos_factory = MacOSFactory()
    macos_button, macos_checkbox = create_gui(macos_factory)
    print(macos_button.render())  # Output: Render a macOS style button
    print(macos_checkbox.render())  # Output: Render a macOS style checkbox
