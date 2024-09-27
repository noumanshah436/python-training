# In Python, the @dataclass decorator is used to automatically generate special methods for classes, 
#   such as __init__, __repr__, __eq__, and others. 
# It simplifies the creation of classes that are primarily used to store data, reducing boilerplate code.



from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

# Create an instance of the Person class
person = Person(name="John Doe", age=30, email="john.doe@example.com")

print(person)  # Output: Person(name='John Doe', age=30, email='john.doe@example.com')


# Key Features:
# Automatic __init__ generation: You don't need to manually write an __init__ method.
# Automatic __repr__ generation: For easy debugging and readable print statements.
# Comparison methods: Methods like __eq__ are automatically generated, allowing instances to be compared using ==.


# ****************************************************************

# The `@dataclass` decorator in Python offers various advanced features and options. Here’s a deeper dive into its capabilities:

# ### 1. **Field Types and Default Values**

# You can specify default values for fields, as well as use special factory functions for mutable default values (like lists or dictionaries).

# ```python
# from dataclasses import dataclass, field
# from typing import List

# @dataclass
# class Student:
#     name: str
#     age: int = 18  # Default value for age
#     subjects: List[str] = field(default_factory=list)  # Avoid mutable default arguments
# ```

# In this case, if you create a `Student` instance without specifying `age`, it will default to 18. The `default_factory` is used to avoid mutable default values like lists or dictionaries (as these could cause unintended side effects).

# ### 2. **The `field()` Function**

# The `field()` function allows for more control over how individual fields behave. For instance, you can specify metadata, whether a field should be included in equality checks, or whether a field should be part of the class's generated `__repr__`.

# ```python
# from dataclasses import dataclass, field

# @dataclass
# class Book:
#     title: str
#     author: str = field(repr=False)  # This field won’t appear in the __repr__ output
#     year: int = field(compare=False)  # This field will be ignored when comparing objects
# ```

# ### 3. **Immutable Data Classes (`frozen=True`)**

# If you want your data class to be immutable (i.e., its fields cannot be modified after instantiation), you can set `frozen=True`. This will cause the generated `__setattr__` method to raise an error if you try to modify any field.

# ```python
# @dataclass(frozen=True)
# class Coordinates:
#     x: float
#     y: float

# coord = Coordinates(10.5, 20.3)
# coord.x = 15.2  # This will raise a FrozenInstanceError
# ```

# ### 4. **Ordering of Objects (`order=True`)**

# You can enable ordering methods (`<`, `<=`, `>`, `>=`) by using `order=True`. This will generate comparison methods based on the fields in the class, in the order they are defined.

# ```python
# @dataclass(order=True)
# class Person:
#     name: str
#     age: int

# p1 = Person("Alice", 25)
# p2 = Person("Bob", 30)

# print(p1 < p2)  # True, because p1.age < p2.age
# ```

# ### 5. **Customization of the `__init__` Method**

# While the `@dataclass` decorator automatically generates an `__init__` method, you can still define your own. This is useful if you need to preprocess data before assigning it to fields.

# ```python
# @dataclass
# class Rectangle:
#     width: float
#     height: float

#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height
#         if width <= 0 or height <= 0:
#             raise ValueError("Width and height must be positive")
# ```

# ### 6. **Post-Initialization with `__post_init__`**

# If you need to do additional processing after the `__init__` method runs, you can define a `__post_init__` method. This method is automatically called after the dataclass has been initialized.

# ```python
# @dataclass
# class Circle:
#     radius: float
#     area: float = field(init=False)

#     def __post_init__(self):
#         self.area = 3.14159 * (self.radius ** 2)
# ```

# In this case, `area` is calculated based on the `radius` provided during initialization, and you don’t have to include `area` as an argument in the `__init__` method because of `init=False`.

# ### 7. **Handling Mutable Default Values**

# In Python, mutable default arguments like lists, dictionaries, or sets can cause subtle bugs when used incorrectly. Using `default_factory` inside `field()` ensures that each instance gets its own new mutable object.

# ```python
# from dataclasses import dataclass, field
# from typing import List

# @dataclass
# class Team:
#     members: List[str] = field(default_factory=list)

# team1 = Team()
# team2 = Team()

# team1.members.append("Alice")
# print(team1.members)  # Output: ['Alice']
# print(team2.members)  # Output: []  (Team2's list is not affected)
# ```

# ### 8. **Inheritance with Data Classes**

# Data classes can be extended through inheritance like regular classes. The child class will inherit all fields from the parent class unless explicitly overridden.

# ```python
# @dataclass
# class Animal:
#     name: str
#     age: int

# @dataclass
# class Dog(Animal):
#     breed: str
# ```

# Here, `Dog` inherits the `name` and `age` fields from `Animal`, and you can add additional fields like `breed`.

# ### 9. **Excluding Fields from Being Compared or Represented**

# You can exclude fields from being included in methods like `__repr__`, `__eq__`, and `__hash__` using the `repr=False`, `compare=False`, or `hash=False` options in `field()`.

# ```python
# @dataclass
# class Person:
#     name: str
#     age: int = field(compare=False)
#     password: str = field(repr=False)
# ```

# - `compare=False`: The `age` field will not be used in equality checks.
# - `repr=False`: The `password` field will not appear in the `__repr__` string.

# ### 10. **Working with `slots`**

# Starting from Python 3.10, data classes support `slots`, which optimize memory usage by preventing the dynamic creation of instance dictionaries. You can enable this by using `slots=True`.

# ```python
# @dataclass(slots=True)
# class Point:
#     x: float
#     y: float
# ```

# This will prevent the class from having a `__dict__`, saving memory in situations where you create many instances of the class.

# ---

# These features allow `@dataclass` to be both concise and highly flexible, making it suitable for a wide range of use cases from simple data containers to more complex classes with behavior.