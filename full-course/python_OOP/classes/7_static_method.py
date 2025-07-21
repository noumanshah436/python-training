"""
Use of Python static method:

We can use a static method for simple functionality that is mostly not related to the class.

static methods can't access class or instance state because they don't take a cls or self argument.

static method, we do not need the self or cls to be passed as the first argument.
Static methods do not have any knowledge related to the class that they are built-in.
Static method cannot alter or change any variable value or state of the class.

Most of the functionalities of the static methods can be performed using a class method. However, we prefer
the static method, at places where it could work to make our program more efficient and faster
as we do not have to pass self as a parameter, so the efficiency of the program increases.
"""


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def mark_attendance(string):
        print("This is good " + string)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

harry.mark_attendance("Present")
Employee.mark_attendance("Present")

# staticmethod(Employee.mark_attendance("present"))


# *******************************

# Class method vs Static Method
# The difference between the Class method and the static method is:

# A class method takes cls as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can't access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
# When to use the class or static method?
# We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
# We generally use static methods to create utility functions.

# *******************************

"""
what is benefit of using static method instead of using simple helper function?


Using a `@staticmethod` vs a simple standalone helper function comes down to design, readability, and context. Here's a breakdown of the **benefits** of using a static method inside a class instead of a regular function:

---

### ✅ **Benefits of `@staticmethod`**

#### 1. **Logical grouping**

Static methods live **inside the class**, which signals they are **related to that class's purpose**, even if they don't need access to instance (`self`) or class (`cls`) data.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

This is better than just throwing `add()` in a global helpers file if it's conceptually tied to math operations.

---

#### 2. **Namespacing**

Static methods avoid cluttering the global namespace and prevent name collisions.

```python
# good
utils.MyClass.format_date()

# bad
format_date()  # which format_date is this?
```

---

#### 3. **Discoverability and Documentation**

They appear in class documentation and IDE auto-complete, making it easier for other developers to find and use them.

```python
# Typing MyClass. in an IDE will show the static method
```

---

#### 4. **Consistency in APIs**

Keeping utility logic within a class maintains a **consistent interface**, especially useful in frameworks or libraries.

```python
user = User.find_by_email("a@b.com")  # staticmethod for querying
```

---

### ❌ When Not to Use `@staticmethod`

* If the method is **totally unrelated** to any class, use a plain helper function instead.
* If you **need instance or class data**, use `@classmethod` or a regular method.

---

### ✅ Rule of Thumb

| Use             | When                                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------- |
| `@staticmethod` | When the function **logically belongs to a class** but doesn't need access to instance/class state |
| Free function   | When the function is **completely independent** of any class logic                                 |


"""






