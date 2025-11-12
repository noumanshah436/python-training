# Python Interview Questions and Answers

## Table of Contents

1. [What is Python? What are its key features and advantages?](#1-what-is-python-what-are-its-key-features-and-advantages)
2. [Explain the difference between Python 2 and Python 3](#2-explain-the-difference-between-python-2-and-python-3)
3. [How do you comment code in Python? What are the different types of comments?](#3-how-do-you-comment-code-in-python-what-are-the-different-types-of-comments)
4. [What is the purpose of indentation in Python code?](#4-what-is-the-purpose-of-indentation-in-python-code)
5. [How do you declare and assign values to variables in Python?](#5-how-do-you-declare-and-assign-values-to-variables-in-python)
6. [Describe the basic data types in Python](#6-describe-the-basic-data-types-in-python)
7. [What are Python data structures? Provide examples of each type](#7-what-are-python-data-structures-provide-examples-of-each-type)
8. [Explain the concept of Python functions and how to define and call them](#8-explain-the-concept-of-python-functions-and-how-to-define-and-call-them)
9. [How do you handle exceptions in Python using try-except blocks?](#9-how-do-you-handle-exceptions-in-python-using-try-except-blocks)
10. [Describe the usage and benefits of Python modules and packages](#10-describe-the-usage-and-benefits-of-python-modules-and-packages)
11. [What is a Python generator? How does it differ from a regular function?](#11-what-is-a-python-generator-how-does-it-differ-from-a-regular-function)
12. [Explain the concept of list comprehension in Python](#12-explain-the-concept-of-list-comprehension-in-python)
13. [How do you read and write files in Python?](#13-how-do-you-read-and-write-files-in-python)
14. [What is the difference between a shallow copy and a deep copy in Python?](#14-what-is-the-difference-between-a-shallow-copy-and-a-deep-copy-in-python)
15. [Describe the concept of object-oriented programming (OOP) in Python](#15-describe-the-concept-of-object-oriented-programming-oop-in-python)
16. [What are constructors in Python classes? How are they different from regular methods?](#16-what-are-constructors-in-python-classes-how-are-they-different-from-regular-methods)
17. [How do you implement inheritance in Python? Provide an example](#17-how-do-you-implement-inheritance-in-python-provide-an-example)
18. [Explain the concept of method overriding in Python](#18-explain-the-concept-of-method-overriding-in-python)
19. [What are decorators in Python? How do they work?](#19-what-are-decorators-in-python-how-do-they-work)
20. [How can you handle command-line arguments in a Python script?](#20-how-can-you-handle-command-line-arguments-in-a-python-script)
21. [What is a lambda function in Python? Provide an example](#21-what-is-a-lambda-function-in-python-provide-an-example)
22. [How do you handle regular expressions in Python?](#22-how-do-you-handle-regular-expressions-in-python)
23. [Explain the concept of multithreading in Python](#23-explain-the-concept-of-multithreading-in-python)
24. [What is the purpose and usage of the "yield" keyword in Python?](#24-what-is-the-purpose-and-usage-of-the-yield-keyword-in-python)
25. [Describe the concept of context managers in Python](#25-describe-the-concept-of-context-managers-in-python)
26. [How can you work with databases in Python? Provide an example using a popular database library](#26-how-can-you-work-with-databases-in-python-provide-an-example-using-a-popular-database-library)
27. [Explain the concept of virtual environments in Python and their importance](#27-explain-the-concept-of-virtual-environments-in-python-and-their-importance)
28. [What is the purpose and usage of the "map" and "filter" functions in Python?](#28-what-is-the-purpose-and-usage-of-the-map-and-filter-functions-in-python)
29. [How do you perform unit testing in Python using the built-in "unittest" module?](#29-how-do-you-perform-unit-testing-in-python-using-the-built-in-unittest-module)
30. [Describe the concept of recursion in Python with an example](#30-describe-the-concept-of-recursion-in-python-with-an-example)

---

## 1. What is Python? What are its key features and advantages?

**Answer:**

Python is a high-level, interpreted, general-purpose programming language created by Guido van Rossum and first released in 1991. It emphasizes code readability and simplicity, making it an excellent choice for both beginners and experienced developers.

**Key Features:**

1. **Interpreted Language**: Python code is executed line by line by an interpreter, which means you don't need to compile it before running. This makes development faster and more flexible.

2. **Dynamically Typed**: Variables don't need explicit type declarations. Python automatically determines the type based on the value assigned.

3. **Object-Oriented**: Python supports OOP principles including classes, inheritance, polymorphism, and encapsulation, but it's also flexible enough to support procedural and functional programming styles.

4. **Extensive Standard Library**: Python comes with a comprehensive standard library (the "batteries included" philosophy) that includes modules for file I/O, networking, databases, web development, and more.

5. **Cross-Platform**: Python runs on Windows, macOS, Linux, and many other operating systems without modification.

6. **Large Ecosystem**: The Python Package Index (PyPI) contains over 400,000 packages for various purposes, from web frameworks (Django, Flask) to data science (NumPy, Pandas) and machine learning (TensorFlow, PyTorch).

**Advantages:**

- **Readability**: Python's syntax is clean and intuitive, reducing the cost of program maintenance
- **Rapid Development**: Less code is needed to accomplish tasks compared to languages like Java or C++
- **Community Support**: Large, active community providing extensive documentation, tutorials, and third-party libraries
- **Versatility**: Used in web development, data science, AI/ML, automation, scripting, game development, and more
- **Integration**: Can easily integrate with other languages and systems through various APIs and tools

---

## 2. Explain the difference between Python 2 and Python 3

**Answer:**

Python 2 and Python 3 are two major versions of Python that are not fully compatible with each other. Python 2 reached end-of-life on January 1, 2020, and is no longer maintained.

**Key Differences:**

1. **Print Statement vs Function**:
   - Python 2: `print "Hello"` (statement)
   - Python 3: `print("Hello")` (function)

2. **Integer Division**:
   - Python 2: `5/2` returns `2` (integer division by default)
   - Python 3: `5/2` returns `2.5` (true division), use `5//2` for integer division

3. **Unicode Support**:
   - Python 2: Strings are ASCII by default, Unicode strings need `u"text"`
   - Python 3: Strings are Unicode by default, bytes need `b"text"`

4. **xrange() vs range()**:
   - Python 2: `xrange()` returns an iterator, `range()` returns a list
   - Python 3: `range()` behaves like Python 2's `xrange()`, `xrange()` doesn't exist

5. **Exception Handling**:
   - Python 2: `except Exception, e:`
   - Python 3: `except Exception as e:`

6. **Input Function**:
   - Python 2: `raw_input()` returns string, `input()` evaluates input
   - Python 3: `input()` always returns string (no `raw_input()`)

7. **Iteration**:
   - Python 2: `.keys()`, `.values()`, `.items()` return lists
   - Python 3: They return dictionary view objects (more memory efficient)

8. **Class Definition**:
   - Python 2: Can define classes without inheriting from `object` (old-style classes)
   - Python 3: All classes are new-style (implicitly inherit from `object`)

**Why Python 3?**
Python 3 was designed to fix fundamental design flaws in Python 2. It's cleaner, more consistent, and better supports modern programming practices. All new projects should use Python 3.

---

## 3. How do you comment code in Python? What are the different types of comments?

**Answer:**

Comments in Python are used to explain code, make it more readable, and are ignored by the interpreter during execution.

**Types of Comments:**

1. **Single-line Comments**: Use `#` for single-line comments. Everything after `#` on that line is ignored.

   Example: `# This is a single-line comment`

2. **Multi-line Comments**: Python doesn't have a dedicated syntax for multi-line comments. Instead, you can:
   - Use multiple `#` symbols on consecutive lines
   - Use triple-quoted strings (`"""` or `'''`) which, if not assigned to a variable, act as docstrings or comments

3. **Inline Comments**: Comments on the same line as code (should be used sparingly and only when necessary for clarity)

4. **Docstrings**: Special triple-quoted strings used to document modules, classes, functions, and methods. They're not technically comments but serve documentation purposes and are accessible via `__doc__` attribute.

**Best Practices:**
- Write clear, concise comments that explain "why" rather than "what"
- Keep comments up-to-date with code changes
- Use docstrings for function/class documentation
- Avoid obvious comments that just restate the code

---

## 4. What is the purpose of indentation in Python code?

**Answer:**

Indentation in Python is not just for readability—it's a fundamental part of the language syntax. Python uses indentation to define code blocks, unlike languages like C, Java, or JavaScript that use curly braces `{}`.

**Purpose:**

1. **Block Delimitation**: Indentation determines which statements belong to which block (functions, loops, conditionals, classes).

2. **Syntax Requirement**: Incorrect indentation causes an `IndentationError` and prevents code from running.

3. **Consistency**: Forces developers to write consistently formatted code, improving readability across projects.

**Rules:**
- Standard practice is to use 4 spaces per indentation level (PEP 8 recommendation)
- Tabs can be used but mixing tabs and spaces causes errors
- All statements at the same level must have the same indentation
- Increase indentation to start a new block, decrease to end it

**Example:**
```python
if condition:
    print("Inside if block")
    if nested_condition:
        print("Nested block")
    print("Back to first level")
print("Outside all blocks")
```

**Why This Design?**
Guido van Rossum chose indentation-based syntax to enforce clean, readable code and eliminate debates about brace placement. It makes Python code more uniform and easier to read across different projects.

---

## 5. How do you declare and assign values to variables in Python?

**Answer:**

In Python, variables don't need explicit declaration. They are created automatically when you first assign a value to them.

**Variable Assignment:**

1. **Basic Assignment**: Use `=` operator
   - `name = "Python"`
   - `age = 30`
   - `price = 99.99`

2. **Multiple Assignment**: Assign same value to multiple variables
   - `x = y = z = 0`

3. **Multiple Variable Assignment**: Assign different values to multiple variables
   - `a, b, c = 1, 2, 3`
   - `name, age = "John", 25`

4. **Unpacking**: Assign values from sequences
   - `x, y = (10, 20)`
   - `first, *rest = [1, 2, 3, 4]`

**Key Characteristics:**

- **Dynamic Typing**: Variables can change type during execution
  - `var = 10` (integer)
  - `var = "hello"` (now string)

- **No Declaration**: No need for `int x;` or `var x;` like in other languages

- **Naming Rules**:
  - Must start with letter or underscore
  - Can contain letters, numbers, underscores
  - Case-sensitive (`name` ≠ `Name`)
  - Cannot use Python keywords (if, for, class, etc.)

- **Memory Management**: Python automatically handles memory allocation and deallocation through garbage collection

**Best Practices:**
- Use descriptive names (`user_age` not `ua`)
- Follow naming conventions (snake_case for variables)
- Initialize variables before use
- Avoid using built-in function names as variable names

---

## 6. Describe the basic data types in Python

**Answer:**

Python has several built-in data types that are fundamental to programming. These are categorized into numeric, sequence, mapping, set, and boolean types.

**Numeric Types:**

1. **int (Integer)**: Whole numbers, positive or negative, of unlimited length
   - Example: `42`, `-100`, `1000000`

2. **float (Floating Point)**: Real numbers with decimal points
   - Example: `3.14`, `-0.5`, `1.0e10` (scientific notation)

3. **complex**: Numbers with real and imaginary parts
   - Example: `3 + 4j`, `complex(3, 4)`

**Sequence Types:**

4. **str (String)**: Sequence of characters, immutable
   - Example: `"Hello"`, `'World'`, `"""Multi-line string"""`

5. **list**: Ordered, mutable collection of items
   - Example: `[1, 2, 3]`, `['a', 'b', 'c']`, `[1, 'mixed', 3.14]`

6. **tuple**: Ordered, immutable collection of items
   - Example: `(1, 2, 3)`, `('a', 'b')`, `(1,)` (single item tuple)

**Mapping Type:**

7. **dict (Dictionary)**: Unordered collection of key-value pairs
   - Example: `{'name': 'John', 'age': 30}`

**Set Types:**

8. **set**: Unordered collection of unique items, mutable
   - Example: `{1, 2, 3}`, `set([1, 2, 3])`

9. **frozenset**: Unordered collection of unique items, immutable
   - Example: `frozenset([1, 2, 3])`

**Boolean Type:**

10. **bool**: Represents truth values (`True` or `False`)
    - Example: `True`, `False`, `bool(1)`, `bool(0)`

**None Type:**

11. **NoneType**: Represents absence of value, only value is `None`
    - Example: `None`

**Type Checking:**
You can check types using `type()` function or `isinstance()` function. The `isinstance()` function is preferred as it handles inheritance properly.

**Type Conversion:**
Python provides built-in functions for type conversion: `int()`, `float()`, `str()`, `list()`, `tuple()`, `dict()`, `set()`, `bool()`, etc.

---

## 7. What are Python data structures? Provide examples of each type

**Answer:**

Data structures are ways of organizing and storing data in Python. They determine how data can be accessed, modified, and organized efficiently.

**Built-in Data Structures:**

1. **List**: Ordered, mutable, allows duplicates
   - Use case: When you need an ordered collection that can change
   - Example: `fruits = ['apple', 'banana', 'orange']`
   - Operations: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`

2. **Tuple**: Ordered, immutable, allows duplicates
   - Use case: When you need an ordered collection that shouldn't change (coordinates, database records)
   - Example: `coordinates = (10, 20)`
   - Operations: `count()`, `index()`, unpacking

3. **Dictionary (dict)**: Unordered, mutable, key-value pairs, keys must be unique
   - Use case: When you need to map keys to values (like a real dictionary)
   - Example: `person = {'name': 'John', 'age': 30}`
   - Operations: `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`

4. **Set**: Unordered, mutable, unique elements only
   - Use case: When you need unique elements and set operations (union, intersection)
   - Example: `unique_numbers = {1, 2, 3, 4, 5}`
   - Operations: `add()`, `remove()`, `union()`, `intersection()`, `difference()`

5. **Frozenset**: Unordered, immutable, unique elements only
   - Use case: When you need an immutable set (can be used as dictionary keys)
   - Example: `immutable_set = frozenset([1, 2, 3])`

**Collections Module (Advanced Data Structures):**

6. **deque**: Double-ended queue, efficient append/pop from both ends
   - Example: `from collections import deque; dq = deque([1, 2, 3])`

7. **Counter**: Dictionary subclass for counting hashable objects
   - Example: `from collections import Counter; c = Counter(['a', 'b', 'a'])`

8. **defaultdict**: Dictionary with default factory function
   - Example: `from collections import defaultdict; dd = defaultdict(list)`

9. **OrderedDict**: Dictionary that remembers insertion order (less relevant in Python 3.7+)
   - Example: `from collections import OrderedDict`

10. **namedtuple**: Tuple subclass with named fields
    - Example: `from collections import namedtuple; Point = namedtuple('Point', ['x', 'y'])`

**When to Use Each:**
- **List**: General-purpose ordered collection
- **Tuple**: Immutable ordered collection (faster, can be dictionary keys)
- **Dictionary**: Key-value mappings, lookups by key
- **Set**: Unique elements, membership testing, set operations
- **deque**: Queue/stack operations
- **Counter**: Counting occurrences
- **defaultdict**: Avoiding KeyError when accessing missing keys

---

## 8. Explain the concept of Python functions and how to define and call them

**Answer:**

Functions in Python are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs more modular and maintainable.

**Defining Functions:**

Functions are defined using the `def` keyword followed by the function name, parentheses containing parameters, and a colon. The function body is indented.

**Basic Syntax:**
```python
def function_name(parameters):
    """Optional docstring describing the function"""
    # Function body
    return value  # Optional
```

**Types of Function Parameters:**

1. **Positional Arguments**: Arguments passed in order
   - `def greet(name, age):`

2. **Default Arguments**: Parameters with default values
   - `def greet(name, age=25):`

3. **Keyword Arguments**: Arguments passed by name
   - `greet(name="John", age=30)`

4. **Variable-length Arguments**:
   - `*args`: Collects extra positional arguments as tuple
   - `**kwargs`: Collects extra keyword arguments as dictionary

**Calling Functions:**

Functions are called by using the function name followed by parentheses containing arguments.

**Examples:**
- `result = function_name(arg1, arg2)`
- `function_name()` (no return value needed)
- `greet("John", 30)` (positional)
- `greet(name="John", age=30)` (keyword)
- `greet("John")` (using default for age)

**Key Concepts:**

1. **Return Statement**: Functions can return values using `return`. If no return statement, function returns `None`.

2. **Multiple Returns**: Functions can return multiple values (as a tuple):
   - `return x, y, z` is equivalent to `return (x, y, z)`

3. **Scope**: Variables defined inside functions are local. Use `global` keyword to modify global variables.

4. **First-class Objects**: Functions are first-class objects in Python, meaning they can be:
   - Assigned to variables
   - Passed as arguments
   - Returned from other functions
   - Stored in data structures

5. **Lambda Functions**: Anonymous functions defined with `lambda` keyword (covered in detail in question 21)

**Best Practices:**
- Use descriptive function names (verbs)
- Keep functions focused on a single task
- Use docstrings to document functions
- Limit the number of parameters (consider using data structures for many parameters)
- Return values rather than modifying global state when possible

---

## 9. How do you handle exceptions in Python using try-except blocks?

**Answer:**

Exception handling in Python allows you to gracefully handle errors and prevent program crashes. It's done using `try-except` blocks.

**Basic Syntax:**
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ExceptionType:
    # Code to handle the exception
    print("An error occurred")
```

**Exception Handling Components:**

1. **try Block**: Contains code that might raise an exception

2. **except Block**: Handles specific exceptions
   - Can specify exception type: `except ValueError:`
   - Can catch multiple exceptions: `except (ValueError, TypeError):`
   - Can use `as` to get exception object: `except ValueError as e:`

3. **else Block**: Executes if no exception occurs (optional)
   ```python
   try:
       result = 10 / 2
   except ZeroDivisionError:
       print("Division by zero")
   else:
       print("No exception occurred")
   ```

4. **finally Block**: Always executes, regardless of exceptions (optional)
   ```python
   try:
       # code
   except:
       # handle
   finally:
       # cleanup code (always runs)
   ```

**Common Built-in Exceptions:**

- `ValueError`: Wrong value type
- `TypeError`: Wrong type operation
- `KeyError`: Dictionary key not found
- `IndexError`: List index out of range
- `FileNotFoundError`: File doesn't exist
- `ZeroDivisionError`: Division by zero
- `AttributeError`: Attribute doesn't exist
- `ImportError`: Module import failed

**Best Practices:**

1. **Be Specific**: Catch specific exceptions rather than bare `except:`
   - Bad: `except:`
   - Good: `except ValueError:`

2. **Don't Suppress Errors**: Always handle or log exceptions appropriately

3. **Use finally for Cleanup**: Use `finally` for resource cleanup (file closing, database connections)

4. **Raise Exceptions**: Use `raise` to raise exceptions when needed
   - `raise ValueError("Invalid input")`

5. **Custom Exceptions**: Create custom exception classes for domain-specific errors
   ```python
   class CustomError(Exception):
       pass
   ```

6. **Exception Chaining**: Use `raise...from` to chain exceptions for better debugging

**Context Managers:**
For resource management, prefer context managers (`with` statement) over try-finally blocks when possible, as they're more Pythonic and cleaner.

---

## 10. Describe the usage and benefits of Python modules and packages

**Answer:**

Modules and packages are fundamental to organizing Python code into reusable, maintainable units.

**Modules:**

A module is a single Python file containing functions, classes, and variables that can be imported and used in other Python programs.

**Creating a Module:**
- Save code in a `.py` file (e.g., `math_utils.py`)
- The filename (without `.py`) becomes the module name

**Importing Modules:**

1. **Import entire module**: `import math`
   - Access: `math.sqrt(16)`

2. **Import specific items**: `from math import sqrt, pi`
   - Access: `sqrt(16)`, `pi`

3. **Import with alias**: `import numpy as np`
   - Access: `np.array([1, 2, 3])`

4. **Import all**: `from math import *` (not recommended)

**Packages:**

A package is a collection of modules organized in directories. A package is a directory containing:
- Multiple `.py` files (modules)
- An `__init__.py` file (makes directory a package, can be empty)

**Package Structure:**
```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

**Benefits:**

1. **Code Reusability**: Write once, use many times across different projects

2. **Organization**: Logical grouping of related functionality

3. **Namespace Management**: Avoid naming conflicts (different modules can have same function names)

4. **Maintainability**: Easier to maintain and update code when organized into modules

5. **Collaboration**: Multiple developers can work on different modules simultaneously

6. **Testing**: Easier to test isolated modules

7. **Standard Library**: Access to Python's extensive standard library modules

8. **Third-party Libraries**: Use packages from PyPI (Python Package Index)

**Standard Library Examples:**
- `os`: Operating system interface
- `sys`: System-specific parameters
- `json`: JSON encoder/decoder
- `datetime`: Date and time handling
- `collections`: Specialized container datatypes
- `itertools`: Iterator functions
- `re`: Regular expressions

**Best Practices:**

1. **Use meaningful names**: Module names should be descriptive
2. **Avoid circular imports**: Module A imports B, B imports A
3. **Use `__init__.py`**: Properly initialize packages
4. **Document modules**: Use docstrings at module level
5. **Follow PEP 8**: Naming conventions for modules (lowercase, underscores)
6. **Virtual environments**: Isolate project dependencies

**Module Search Path:**
Python searches for modules in:
1. Current directory
2. Directories in `PYTHONPATH` environment variable
3. Standard library directories
4. Site-packages directory (third-party packages)

---

## 11. What is a Python generator? How does it differ from a regular function?

**Answer:**

A generator is a special type of function that returns an iterator. Instead of returning a value and terminating, generators use the `yield` keyword to produce a sequence of values one at a time, maintaining their state between calls.

**Key Differences:**

1. **Memory Efficiency**: 
   - Regular functions: Return all values at once, storing them in memory
   - Generators: Produce values on-demand, one at a time, using minimal memory

2. **Execution Flow**:
   - Regular functions: Execute completely, return result, lose state
   - Generators: Pause at `yield`, resume from that point on next call

3. **Return Type**:
   - Regular functions: Return a value
   - Generators: Return a generator object (iterator)

4. **State Preservation**:
   - Regular functions: Don't remember previous calls
   - Generators: Remember state between calls

**Creating Generators:**

1. **Generator Functions**: Use `yield` instead of `return`
   ```python
   def count_up_to(max):
       count = 1
       while count <= max:
           yield count
           count += 1
   ```

2. **Generator Expressions**: Similar to list comprehensions but with parentheses
   ```python
   squares = (x**2 for x in range(10))
   ```

**How Generators Work:**

1. When called, generator function returns a generator object (doesn't execute immediately)
2. Code executes until first `yield` statement
3. Function pauses, returns yielded value
4. On next call (via `next()` or iteration), resumes after `yield`
5. Continues until function ends or `return` statement

**Use Cases:**

1. **Large Datasets**: Processing files line by line, database records
2. **Infinite Sequences**: Generating infinite sequences (Fibonacci, prime numbers)
3. **Memory Constraints**: When you can't load all data into memory
4. **Pipelines**: Chaining generators for data processing pipelines
5. **Lazy Evaluation**: Computing values only when needed

**Advantages:**

- **Memory Efficient**: Don't store entire sequence in memory
- **Lazy Evaluation**: Values computed on-demand
- **Composable**: Can chain generators together
- **Stateful**: Maintain state between calls

**Limitations:**

- **One-time Use**: Generator objects can only be iterated once
- **No Random Access**: Can't access arbitrary indices
- **No Length**: Don't have `len()` method

**Example Use Case:**
Reading a large file line by line instead of loading entire file into memory:
```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

---

## 12. Explain the concept of list comprehension in Python

**Answer:**

List comprehension is a concise, Pythonic way to create lists. It provides a more readable and efficient alternative to traditional loops for creating lists.

**Basic Syntax:**
```python
[expression for item in iterable]
```

**Components:**
1. **Expression**: What to do with each item
2. **for item in iterable**: Loop through items
3. **Optional conditions**: Filter items

**Examples:**

1. **Basic List Comprehension**:
   - Traditional: `squares = [x**2 for x in range(10)]`
   - Equivalent to:
     ```python
     squares = []
     for x in range(10):
         squares.append(x**2)
     ```

2. **With Condition (Filtering)**:
   - `even_squares = [x**2 for x in range(10) if x % 2 == 0]`
   - Only includes squares of even numbers

3. **With Conditional Expression**:
   - `result = [x if x > 0 else 0 for x in numbers]`
   - Ternary operator in comprehension

4. **Nested Comprehensions**:
   - `matrix = [[i*j for j in range(3)] for i in range(3)]`
   - Creates nested lists

**Advantages:**

1. **Readability**: More concise and readable than loops
2. **Performance**: Generally faster than equivalent loops
3. **Pythonic**: Follows Python's philosophy of clean, readable code
4. **Functional Style**: Encourages functional programming patterns

**Other Comprehensions:**

Python also supports:
- **Dictionary Comprehension**: `{key: value for item in iterable}`
- **Set Comprehension**: `{expression for item in iterable}`
- **Generator Expression**: `(expression for item in iterable)` (uses parentheses)

**When to Use:**

- **Use List Comprehension**: For simple transformations and filtering
- **Avoid**: When logic is complex (use regular loops for clarity)
- **Avoid**: When you need side effects (use loops)

**Best Practices:**

1. Keep comprehensions readable (don't nest too deeply)
2. Use for simple transformations
3. Prefer generator expressions for large datasets (memory efficient)
4. Don't sacrifice readability for brevity

**Example:**
```python
# Filter and transform
names = ['Alice', 'Bob', 'Charlie', 'David']
upper_names = [name.upper() for name in names if len(name) > 3]
# Result: ['ALICE', 'CHARLIE', 'DAVID']
```

---

## 13. How do you read and write files in Python?

**Answer:**

File operations in Python are straightforward and can be done using built-in functions. The recommended approach is using context managers (`with` statement) for automatic resource management.

**Opening Files:**

Use the `open()` function:
```python
file = open('filename.txt', 'mode')
```

**File Modes:**

- `'r'`: Read (default, text mode)
- `'w'`: Write (overwrites existing file)
- `'a'`: Append (adds to end of file)
- `'x'`: Exclusive creation (fails if file exists)
- `'b'`: Binary mode (e.g., `'rb'`, `'wb'`)
- `'t'`: Text mode (default)
- `'+'`: Read and write (e.g., `'r+'`)

**Reading Files:**

1. **Read Entire File**:
   ```python
   with open('file.txt', 'r') as f:
       content = f.read()
   ```

2. **Read Line by Line**:
   ```python
   with open('file.txt', 'r') as f:
       for line in f:
           print(line.strip())
   ```

3. **Read All Lines into List**:
   ```python
   with open('file.txt', 'r') as f:
       lines = f.readlines()
   ```

4. **Read Single Line**:
   ```python
   with open('file.txt', 'r') as f:
       first_line = f.readline()
   ```

**Writing Files:**

1. **Write Text**:
   ```python
   with open('file.txt', 'w') as f:
       f.write('Hello, World!')
   ```

2. **Write Multiple Lines**:
   ```python
   with open('file.txt', 'w') as f:
       f.write('Line 1\n')
       f.write('Line 2\n')
   ```

3. **Write List of Lines**:
   ```python
   lines = ['Line 1\n', 'Line 2\n']
   with open('file.txt', 'w') as f:
       f.writelines(lines)
   ```

**Context Managers (Recommended):**

The `with` statement automatically handles file closing, even if an exception occurs:
```python
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed here
```

**Benefits of Context Managers:**
- Automatic file closing
- Exception safety
- Cleaner code
- No need for `try-finally` blocks

**File Object Methods:**

- `read(size)`: Read specified number of bytes/characters
- `readline()`: Read single line
- `readlines()`: Read all lines into list
- `write(string)`: Write string to file
- `writelines(list)`: Write list of strings
- `seek(offset)`: Change file position
- `tell()`: Get current file position
- `close()`: Close file

**Error Handling:**

Always handle potential file errors:
```python
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except IOError:
    print("I/O error occurred")
```

**Best Practices:**

1. Always use context managers (`with` statement)
2. Handle file exceptions appropriately
3. Specify encoding for text files: `open('file.txt', 'r', encoding='utf-8')`
4. Use binary mode for non-text files (images, executables)
5. Don't forget newline characters (`\n`) when writing
6. Use `pathlib` module (Python 3.4+) for modern path handling

**Working with Paths:**

Modern approach using `pathlib`:
```python
from pathlib import Path

file_path = Path('data/file.txt')
content = file_path.read_text()
file_path.write_text('New content')
```

---

## 14. What is the difference between a shallow copy and a deep copy in Python?

**Answer:**

Understanding the difference between shallow and deep copies is crucial when working with mutable objects like lists and dictionaries, as it affects how changes to copied objects impact the original.

**Shallow Copy:**

A shallow copy creates a new object but inserts references to the objects found in the original. For nested structures, only the top-level is copied, while nested objects are referenced.

**Characteristics:**
- Creates a new container object
- Copies references to nested objects (not the objects themselves)
- Changes to nested objects affect both original and copy
- Changes to top-level items don't affect each other

**Creating Shallow Copies:**
- Lists: `new_list = original_list.copy()` or `new_list = list(original_list)` or `new_list = original_list[:]`
- Dictionaries: `new_dict = original_dict.copy()` or `new_dict = dict(original_dict)`
- General: `import copy; new_obj = copy.copy(original_obj)`

**Example:**
```python
original = [[1, 2, 3], [4, 5, 6]]
shallow = original.copy()
shallow[0][0] = 99
# Both original and shallow now have [[99, 2, 3], [4, 5, 6]]
```

**Deep Copy:**

A deep copy creates a new object and recursively copies all nested objects. It's a completely independent copy.

**Characteristics:**
- Creates a new container object
- Recursively copies all nested objects
- Completely independent from original
- Changes to copy don't affect original and vice versa

**Creating Deep Copies:**
```python
import copy
new_obj = copy.deepcopy(original_obj)
```

**Example:**
```python
original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)
deep[0][0] = 99
# Only deep is changed: [[99, 2, 3], [4, 5, 6]]
# Original remains: [[1, 2, 3], [4, 5, 6]]
```

**When to Use Each:**

**Use Shallow Copy When:**
- Working with flat structures (no nesting)
- You want to share nested objects
- Performance is critical (deep copy is slower)
- Objects contain immutable nested items

**Use Deep Copy When:**
- Working with nested mutable structures
- You need complete independence
- Modifying nested objects shouldn't affect original
- Working with complex object hierarchies

**Important Notes:**

1. **Immutable Types**: For immutable types (int, str, tuple), shallow and deep copy behave the same (no practical difference)

2. **Assignment vs Copy**: 
   - Assignment (`new = original`): Creates a reference, not a copy
   - Both variables point to same object

3. **Performance**: Deep copy is slower and uses more memory, especially for large nested structures

4. **Custom Objects**: For custom classes, you may need to implement `__copy__()` and `__deepcopy__()` methods

**Example Scenario:**
```python
# Assignment (not a copy)
list1 = [[1, 2], [3, 4]]
list2 = list1  # Both reference same object

# Shallow copy
list3 = list1.copy()  # New list, but nested lists are shared

# Deep copy
import copy
list4 = copy.deepcopy(list1)  # Completely independent
```

---

## 15. Describe the concept of object-oriented programming (OOP) in Python

**Answer:**

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects and classes. Python is a multi-paradigm language that fully supports OOP principles.

**Core OOP Concepts:**

1. **Classes**: Blueprints for creating objects. Define attributes (data) and methods (functions) that objects will have.

2. **Objects (Instances)**: Specific instances created from a class. Each object has its own set of attributes.

3. **Encapsulation**: Bundling data and methods that operate on that data within a single unit (class). Access control through public, protected, and private attributes.

4. **Inheritance**: Mechanism where a class (child/derived) inherits attributes and methods from another class (parent/base). Promotes code reuse.

5. **Polymorphism**: Ability of different classes to be used through the same interface. "One interface, many implementations."

6. **Abstraction**: Hiding complex implementation details and showing only essential features.

**Python OOP Features:**

**Class Definition:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"
```

**Key Characteristics:**

1. **`self` Parameter**: First parameter of instance methods, refers to the instance itself

2. **`__init__` Method**: Constructor method, called when object is created

3. **Instance Variables**: Attributes unique to each instance (`self.name`)

4. **Class Variables**: Shared across all instances (defined outside `__init__`)

5. **Methods**: Functions defined within a class
   - Instance methods: Operate on instance data
   - Class methods: Operate on class data (`@classmethod`)
   - Static methods: Don't need instance or class (`@staticmethod`)

**Access Modifiers (Convention-based):**

Python doesn't enforce access modifiers but uses naming conventions:
- **Public**: `attribute` (no prefix)
- **Protected**: `_attribute` (single underscore, convention)
- **Private**: `__attribute` (double underscore, name mangling)

**Special Methods (Magic Methods):**

Python provides special methods for operator overloading and built-in behavior:
- `__str__()`: String representation
- `__repr__()`: Official string representation
- `__len__()`: Length of object
- `__eq__()`: Equality comparison
- `__add__()`: Addition operator
- And many more...

**Benefits of OOP:**

1. **Modularity**: Code organized into logical units
2. **Reusability**: Classes can be reused across projects
3. **Maintainability**: Easier to maintain and update
4. **Scalability**: Easier to extend functionality
5. **Abstraction**: Hide complexity, expose simple interface
6. **Modeling**: Better represents real-world entities

**Python OOP Advantages:**

- Dynamic: Can add attributes/methods at runtime
- Multiple inheritance supported
- Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"
- Mixins: Reusable components through multiple inheritance
- Properties: Use `@property` decorator for getters/setters

**Best Practices:**

1. Follow naming conventions (PascalCase for classes)
2. Use docstrings for classes and methods
3. Keep classes focused (Single Responsibility Principle)
4. Prefer composition over inheritance when appropriate
5. Use properties instead of direct attribute access when needed
6. Implement `__str__` and `__repr__` for better debugging

**Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Polymorphism
animals = [Dog("Buddy"), Dog("Max")]
for animal in animals:
    print(animal.speak())
```

---

## 16. What are constructors in Python classes? How are they different from regular methods?

**Answer:**

Constructors are special methods in Python classes that are automatically called when an object (instance) is created. They initialize the object's attributes and set up the initial state.

**The `__init__` Method:**

In Python, the constructor is the `__init__` method (short for "initialize"). It's not technically a constructor in the traditional sense (that would be `__new__`), but it's what most developers refer to as the constructor.

**Key Characteristics:**

1. **Automatic Invocation**: Called automatically when you create an object
   ```python
   obj = MyClass()  # __init__ is called automatically
   ```

2. **First Parameter `self`**: Always takes `self` as the first parameter (reference to the instance)

3. **Initialization**: Used to set initial values for instance attributes

4. **Optional**: Not required—if not defined, Python uses default constructor

**Basic Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person object created")

# Creating object calls __init__
person = Person("John", 30)
```

**Differences from Regular Methods:**

1. **Automatic Execution**:
   - Constructor: Called automatically on object creation
   - Regular method: Must be called explicitly

2. **Naming**:
   - Constructor: Must be named `__init__`
   - Regular method: Any valid name

3. **Purpose**:
   - Constructor: Initialize object state
   - Regular method: Perform operations on/with the object

4. **Return Value**:
   - Constructor: Should not return a value (returns `None` implicitly)
   - Regular method: Can return any value

5. **Calling**:
   - Constructor: Called via class instantiation
   - Regular method: Called on instance using dot notation

6. **Frequency**:
   - Constructor: Called once per object creation
   - Regular method: Can be called multiple times

**The `__new__` Method:**

Python actually has two methods involved in object creation:
- `__new__()`: Creates the instance (true constructor, rarely overridden)
- `__init__()`: Initializes the instance (what we typically call constructor)

**Default Constructor:**

If you don't define `__init__`, Python provides a default one that does nothing:
```python
class SimpleClass:
    pass  # Has default __init__ that does nothing
```

**Constructor with Default Values:**
```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
```

**Constructor Best Practices:**

1. Initialize all instance attributes in `__init__`
2. Use default parameters for optional attributes
3. Don't perform heavy computations in constructor
4. Keep constructor simple and focused on initialization
5. Document parameters with docstrings
6. Validate input parameters when necessary

**Example Comparison:**
```python
class Calculator:
    def __init__(self, initial_value=0):  # Constructor
        self.value = initial_value
        print("Calculator initialized")
    
    def add(self, number):  # Regular method
        self.value += number
        return self.value
    
    def reset(self):  # Regular method
        self.value = 0

# Constructor called automatically
calc = Calculator(10)  # Prints: "Calculator initialized"

# Regular methods called explicitly
result = calc.add(5)  # Must call explicitly
calc.reset()  # Must call explicitly
```

---

## 17. How do you implement inheritance in Python? Provide an example

**Answer:**

Inheritance is a fundamental OOP concept that allows a class (child/derived/subclass) to inherit attributes and methods from another class (parent/base/superclass). This promotes code reuse and establishes relationships between classes.

**Basic Inheritance Syntax:**

```python
class ParentClass:
    # Parent class definition
    pass

class ChildClass(ParentClass):
    # Child class inherits from ParentClass
    pass
```

**How Inheritance Works:**

1. **Child class inherits all attributes and methods** from parent class
2. **Child can override** parent methods (method overriding)
3. **Child can add new** attributes and methods
4. **Child can extend** parent functionality

**Example:**
```python
# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return "Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} is fetching!"

# Another child class
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")
    
    def make_sound(self):  # Override parent method
        return "Meow!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.info())  # Inherited method
print(dog.make_sound())  # Overridden method
print(dog.fetch())  # D



# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.info())  # Inherited method
print(dog.make_sound())  # Overridden method
print(dog.fetch())  # Dog-specific method

cat = Cat("Whiskers")
print(cat.info())  # Inherited method
print(cat.make_sound())  # Overridden method
```

**Key Concepts:**

1. **`super()` Function**: Used to call parent class methods, especially the constructor. `super().__init__()` calls the parent's `__init__` method.

2. **Method Overriding**: Child class can redefine parent methods with same name.

3. **Method Resolution Order (MRO)**: Python determines which method to call when multiple inheritance is involved.

4. **Multiple Inheritance**: Python supports inheriting from multiple parent classes:
   ```python
   class ChildClass(Parent1, Parent2):
       pass
   ```

5. **Inheritance Chain**: Can have multi-level inheritance (grandparent → parent → child).

**Benefits:**
- Code reusability
- Logical organization
- Polymorphism support
- Easier maintenance

**Best Practices:**
- Use `super()` to call parent methods
- Don't override unnecessarily
- Keep inheritance hierarchies shallow
- Prefer composition over deep inheritance when appropriate

---

## 18. Explain the concept of method overriding in Python

**Answer:**

Method overriding is an OOP feature where a child class provides a specific implementation of a method that is already defined in its parent class. The overridden method in the child class replaces the parent's method when called on a child class instance.

**How It Works:**

When a child class defines a method with the same name as a method in the parent class, the child's method takes precedence. This allows child classes to customize behavior inherited from parent classes.

**Basic Example:**

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"
    
    def move(self):
        return "Animal is moving"

class Dog(Animal):
    def make_sound(self):  # Overriding parent's make_sound
        return "Woof!"
    
    # move() is inherited, not overridden

class Cat(Animal):
    def make_sound(self):  # Overriding parent's make_sound
        return "Meow!"

# Usage
dog = Dog()
print(dog.make_sound())  # Output: "Woof!" (uses overridden method)
print(dog.move())  # Output: "Animal is moving" (uses inherited method)
```

**Key Characteristics:**

1. **Same Method Signature**: Overridden method should have the same name and parameters as parent method (though Python doesn't enforce this strictly).

2. **Runtime Polymorphism**: The method called depends on the object's type, not the reference type.

3. **Complete Replacement**: Overridden method completely replaces parent method for that class.

4. **Access to Parent Method**: Can still call parent method using `super()`.

**Calling Parent Method:**

You can call the parent's overridden method using `super()`:

```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        parent_sound = super().make_sound()  # Call parent method
        return f"{parent_sound} - Woof!"

dog = Dog()
print(dog.make_sound())  # Output: "Some sound - Woof!"
```

**When to Override:**

1. **Customize Behavior**: When child class needs different behavior than parent
2. **Extend Functionality**: Add to parent's functionality while keeping base behavior
3. **Implement Abstract Methods**: Provide implementation for abstract methods
4. **Fix Parent Behavior**: Correct or improve parent's implementation

**Method Overriding vs Method Overloading:**

- **Overriding** (Python supports): Same method name, different implementation in child class
- **Overloading** (Python doesn't support): Same method name with different parameters in same class

**Best Practices:**

1. Maintain the same method signature when possible
2. Document why you're overriding
3. Use `super()` to extend rather than completely replace when appropriate
4. Ensure overridden method maintains the same contract/interface
5. Consider using abstract base classes for required overrides

**Example with `__str__` Override:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person: {self.name}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def __str__(self):  # Override parent's __str__
        return f"Student: {self.name} (ID: {self.student_id})"

student = Student("Alice", 20, "S123")
print(student)  # Output: "Student: Alice (ID: S123)"
```

---

## 19. What are decorators in Python? How do they work?

**Answer:**

Decorators are a powerful Python feature that allows you to modify or extend the behavior of functions or methods without permanently modifying them. They're essentially functions that take another function as input and return a modified function.

**Basic Concept:**

A decorator is a design pattern that wraps a function to extend its behavior. In Python, decorators are implemented using the `@` symbol syntax, which is syntactic sugar for function composition.

**How Decorators Work:**

1. **Function as First-Class Object**: In Python, functions are first-class objects, meaning they can be:
   - Assigned to variables
   - Passed as arguments
   - Returned from functions
   - Stored in data structures

2. **Decorator Function**: A decorator is a function that:
   - Takes a function as an argument
   - Defines a wrapper function inside
   - Returns the wrapper function

**Basic Example:**

```python
def my_decorator(func):
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before function
# Hello!
# Something after function
```

**The `@` Syntax:**

The `@decorator` syntax is equivalent to:
```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
```

**Decorators with Arguments:**

When the decorated function takes arguments, the wrapper must accept and pass them:

```python
def smart_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

result = add(5, 3)  # Works with arguments
```

**Common Use Cases:**

1. **Timing Functions**: Measure execution time
   ```python
   import time
   def timer(func):
       def wrapper(*args, **kwargs):
           start = time.time()
           result = func(*args, **kwargs)
           end = time.time()
           print(f"{func.__name__} took {end-start} seconds")
           return result
       return wrapper
   ```

2. **Logging**: Log function calls
   ```python
   def logger(func):
       def wrapper(*args, **kwargs):
           print(f"Calling {func.__name__} with {args}, {kwargs}")
           return func(*args, **kwargs)
       return wrapper
   ```

3. **Authentication/Authorization**: Check permissions before execution

4. **Caching/Memoization**: Store function results

5. **Validation**: Validate inputs before execution

**Built-in Decorators:**

1. **`@property`**: Converts method to property (getter)
2. **`@staticmethod`**: Defines static method (no `self` or `cls`)
3. **`@classmethod`**: Defines class method (takes `cls` instead of `self`)
4. **`@functools.lru_cache`**: Caches function results
5. **`@functools.wraps`**: Preserves function metadata

**Preserving Function Metadata:**

Use `functools.wraps` to preserve original function's metadata:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**Decorator with Arguments:**

You can create decorators that accept arguments by adding another layer:

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints 3 times
```

**Class-Based Decorators:**

Decorators can also be implemented as classes:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")
```

**Multiple Decorators:**

You can stack multiple decorators (applied bottom to top):

```python
@decorator1
@decorator2
@decorator3
def my_function():
    pass
```

**Best Practices:**

1. Use `functools.wraps` to preserve metadata
2. Make decorators reusable and generic
3. Document what the decorator does
4. Handle exceptions appropriately
5. Consider using `functools.lru_cache` for caching needs

**Real-World Example:**

```python
from functools import wraps
import time

def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed, retrying...")
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    # Might fail
    pass
```

---

## 20. How can you handle command-line arguments in a Python script?

**Answer:**

Python provides several ways to handle command-line arguments, from simple to advanced. The most common approaches are using `sys.argv` for basic needs and the `argparse` module for complex argument parsing.

**1. Using `sys.argv` (Simple Approach):**

The `sys.argv` list contains command-line arguments. `sys.argv[0]` is the script name, and subsequent elements are the arguments.

```python
import sys

# python script.py arg1 arg2 arg3
# sys.argv = ['script.py', 'arg1', 'arg2', 'arg3']

if len(sys.argv) > 1:
    first_arg = sys.argv[1]
    print(f"First argument: {first_arg}")
else:
    print("No arguments provided")
```

**Limitations:**
- No automatic type conversion
- No help messages
- Manual parsing required
- No validation

**2. Using `argparse` (Recommended):**

The `argparse` module provides a powerful, user-friendly way to handle command-line arguments with automatic help generation, type conversion, and validation.

**Basic Example:**

```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

**Key `argparse` Features:**

1. **Positional Arguments:**
   ```python
   parser.add_argument('filename', help='Input file name')
   ```

2. **Optional Arguments:**
   ```python
   parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
   ```

3. **Arguments with Values:**
   ```python
   parser.add_argument('--count', type=int, default=1,
                       help='Number of times to run')
   ```

4. **Choices:**
   ```python
   parser.add_argument('--mode', choices=['read', 'write'],
                       help='Operation mode')
   ```

5. **Required Arguments:**
   ```python
   parser.add_argument('--required-arg', required=True)
   ```

**Common `argparse` Patterns:**

```python
import argparse

parser = argparse.ArgumentParser(
    description='A sample script with command-line arguments'
)

# Positional argument
parser.add_argument('input_file', help='Input file path')

# Optional flag
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Verbose output')

# Optional argument with default
parser.add_argument('-o', '--output', default='output.txt',
                    help='Output file (default: output.txt)')

# Argument with type
parser.add_argument('--count', type=int, default=1,
                    help='Number of iterations')

# Argument with choices
parser.add_argument('--format', choices=['json', 'xml', 'csv'],
                    default='json', help='Output format')

args = parser.parse_args()

# Usage: python script.py input.txt -v --count 5 --format xml
```

**3. Using `getopt` (Legacy):**

Similar to C's `getopt()`, but `argparse` is generally preferred:

```python
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
```

**Best Practices:**

1. **Use `argparse`**: For most applications, `argparse` is the best choice
2. **Provide Help**: Always include `help` descriptions
3. **Set Defaults**: Provide sensible defaults for optional arguments
4. **Validate Input**: Use `type` parameter for automatic validation
5. **Use Short and Long Options**: Provide both `-v` and `--verbose`
6. **Handle Errors**: `argparse` automatically handles errors and shows help

**Example: Complete Script**

```python
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description='Process and analyze data files',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose mode')
    parser.add_argument('--format', choices=['json', 'csv'],
                        default='json', help='Output format')
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Processing {args.input}")
    
    # Your script logic here
    print(f"Input: {args.input}")
    if args.output:
        print(f"Output: {args.output}")
    print(f"Format: {args.format}")

if __name__ == '__main__':
    main()
```

**Accessing Arguments:**

After parsing, access arguments as attributes of the `args` object:
- `args.input` - positional argument
- `args.verbose` - boolean flag
- `args.output` - optional argument
- `args.format` - choice argument

**Error Handling:**

`argparse` automatically:
- Shows help message for `-h` or `--help`
- Validates argument types
- Checks required arguments
- Validates choices
- Shows error messages for invalid input

---

## 21. What is a lambda function in Python? Provide an example

**Answer:**

A lambda function (also called an anonymous function) is a small, unnamed function defined using the `lambda` keyword. It can have any number of arguments but only one expression, which is evaluated and returned.

**Syntax:**

```python
lambda arguments: expression
```

**Key Characteristics:**

1. **Anonymous**: No function name required
2. **Single Expression**: Can only contain one expression (no statements)
3. **Implicit Return**: Expression result is automatically returned
4. **First-Class Object**: Can be assigned to variables, passed as arguments, returned from functions

**Basic Examples:**

1. **Simple Lambda:**
   ```python
   # Regular function
   def add(x, y):
       return x + y
   
   # Equivalent lambda
   add = lambda x, y: x + y
   
   print(add(5, 3))  # Output: 8
   ```

2. **Lambda with One Argument:**
   ```python
   square = lambda x: x ** 2
   print(square(5))  # Output: 25
   ```

3. **Lambda with No Arguments:**
   ```python
   greet = lambda: "Hello, World!"
   print(greet())  # Output: "Hello, World!"
   ```

**Common Use Cases:**

1. **With `map()` Function:**
   ```python
   numbers = [1, 2, 3, 4, 5]
   squared = list(map(lambda x: x ** 2, numbers))
   # Result: [1, 4, 9, 16, 25]
   ```

2. **With `filter()` Function:**
   ```python
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   # Result: [2, 4, 6, 8, 10]
   ```

3. **With `sorted()` Function:**
   ```python
   students = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]
   sorted_by_age = sorted(students, key=lambda x: x[1])
   # Result: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]
   ```

4. **With `reduce()` Function:**
   ```python
   from functools import reduce
   numbers = [1, 2, 3, 4, 5]
   product = reduce(lambda x, y: x * y, numbers)
   # Result: 120
   ```

5. **As Callback Functions:**
   ```python
   button.on_click(lambda: print("Button clicked!"))
   ```

6. **In List Comprehensions (Alternative):**
   ```python
   # Using lambda with map
   squares = list(map(lambda x: x**2, range(10)))
   
   # Equivalent list comprehension (preferred)
   squares = [x**2 for x in range(10)]
   ```

**Lambda vs Regular Functions:**

**Lambda Advantages:**
- Concise for simple operations
- No need to define a function name
- Useful for one-time use functions

**Lambda Limitations:**
- Only one expression (no statements like `if`, `for`, `while`)
- No docstrings
- Less readable for complex logic
- Can't contain `return`, `pass`, `assert`, etc.

**When to Use Lambda:**

✅ **Good for:**
- Simple transformations (`lambda x: x * 2`)
- Filtering conditions (`lambda x: x > 0`)
- Sorting keys (`lambda x: x.name`)
- Callback functions
- One-time use functions

---

## 22. How do you handle regular expressions in Python?

**Answer:**

Python provides the `re` module for working with regular expressions (regex), which are patterns used to match and manipulate strings.

**Basic Usage:**

```python
import re

# Search for pattern
text = "The price is $50"
match = re.search(r'\$(\d+)', text)
if match:
    print(match.group(1))  # Output: "50"

# Find all matches
numbers = re.findall(r'\d+', "I have 5 apples and 3 oranges")
# Result: ['5', '3']

# Replace patterns
text = re.sub(r'\d+', 'X', "I have 5 apples")
# Result: "I have X apples"

# Split by pattern
words = re.split(r'\s+', "hello   world")
# Result: ['hello', 'world']
```

**Common Functions:**
- `re.search()`: Find first match
- `re.findall()`: Find all matches
- `re.match()`: Match at string start
- `re.sub()`: Replace matches
- `re.split()`: Split by pattern
- `re.compile()`: Compile pattern for reuse

**Pattern Flags:**
- `re.IGNORECASE` or `re.I`: Case-insensitive matching
- `re.MULTILINE` or `re.M`: Multi-line matching
- `re.DOTALL` or `re.S`: `.` matches newline

**Best Practices:**
- Use raw strings (`r'pattern'`) to avoid escaping issues
- Compile patterns with `re.compile()` if used multiple times
- Handle `None` when using `match()` or `search()`
- Use `findall()` or `finditer()` for multiple matches

---

## 23. Explain the concept of multithreading in Python

**Answer:**

Multithreading allows a program to run multiple threads (lightweight processes) concurrently. Python's `threading` module provides thread-based parallelism.

**Key Concepts:**

1. **Global Interpreter Lock (GIL)**: Python's GIL allows only one thread to execute Python bytecode at a time, limiting true parallelism for CPU-bound tasks. However, threads are still useful for I/O-bound operations.

2. **Thread Creation:**
   ```python
   import threading
   
   def worker():
       print("Thread executing")
   
   thread = threading.Thread(target=worker)
   thread.start()
   thread.join()  # Wait for thread to complete
   ```

3. **Thread Synchronization:**
   - **Locks**: Prevent race conditions
     ```python
     lock = threading.Lock()
     with lock:
         # Critical section
         pass
     ```
   - **Semaphores**: Control access to resources
   - **Events**: Thread communication
   - **Queues**: Thread-safe data exchange

**When to Use:**
- ✅ I/O-bound tasks (file operations, network requests, database queries)
- ✅ Tasks that wait for external resources
- ❌ CPU-bound tasks (use `multiprocessing` instead)

**Limitations:**
- GIL prevents true parallelism for CPU-bound tasks
- Thread overhead for simple tasks
- Potential race conditions without proper synchronization

**Alternative:**
For CPU-bound tasks, use `multiprocessing` module which uses separate processes (bypasses GIL).

---

## 24. What is the purpose and usage of the "yield" keyword in Python?

**Answer:**

The `yield` keyword is used to create generator functions. It pauses function execution, returns a value, and resumes from that point on the next call.

**Basic Usage:**

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Pauses here, returns count
        count += 1   # Resumes here on next call

# Usage
counter = count_up_to(5)
for num in counter:
    print(num)  # Output: 1, 2, 3, 4, 5
```

**Key Characteristics:**

1. **Memory Efficient**: Generates values on-demand, doesn't store entire sequence
2. **State Preservation**: Function remembers where it paused
3. **Lazy Evaluation**: Values computed only when needed
4. **Returns Generator Object**: Function becomes a generator when `yield` is used

**Common Use Cases:**

- **Large Datasets**: Process files line-by-line without loading entire file
  ```python
  def read_large_file(filename):
      with open(filename) as f:
          for line in f:
              yield line.strip()
  ```

- **Infinite Sequences**: Generate infinite sequences
  ```python
  def fibonacci():
      a, b = 0, 1
      while True:
          yield a
          a, b = b, a + b
  ```

- **Memory-Efficient Processing**: Process data in chunks

**`yield` vs `return`:**
- `return`: Ends function, returns value, loses state
- `yield`: Pauses function, returns value, preserves state for next call

**Generator Expressions:**
Similar to list comprehensions but with parentheses:
```python
squares = (x**2 for x in range(10))  # Generator, not list
```

---

## 25. Describe the concept of context managers in Python

**Answer:**

Context managers are objects that define what happens before and after a block of code executes. They're used with the `with` statement to ensure proper resource management.

**Basic Usage:**

```python
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed here, even if exception occurs
```

**How It Works:**

Context managers implement the context manager protocol with two methods:
- `__enter__()`: Called when entering `with` block
- `__exit__()`: Called when exiting `with` block (even on exceptions)

**Creating Custom Context Managers:**

1. **Class-Based:**
   ```python
   class MyContextManager:
       def __enter__(self):
           print("Entering context")
           return self
       
       def __exit__(self, exc_type, exc_val, exc_tb):
           print("Exiting context")
           return False  # Don't suppress exceptions
   
   with MyContextManager() as cm:
       print("Inside context")
   ```

2. **Using `contextlib.contextmanager` Decorator:**
   ```python
   from contextlib import contextmanager
   
   @contextmanager
   def my_context():
       print("Entering")
       yield
       print("Exiting")
   
   with my_context():
       print("Inside")
   ```

**Common Use Cases:**

- **File Operations**: Automatic file closing
- **Database Connections**: Automatic connection cleanup
- **Locks**: Automatic lock release
- **Temporary Changes**: Revert changes after block
- **Resource Management**: Any resource that needs cleanup

**Built-in Context Managers:**

- `open()`: File operations
- `threading.Lock()`: Thread synchronization
- `contextlib.suppress()`: Suppress exceptions
- `contextlib.redirect_stdout()`: Redirect output

**Benefits:**
- Automatic resource cleanup
- Exception safety
- Cleaner code than try-finally
- Prevents resource leaks

---

## 26. How can you work with databases in Python? Provide an example using a popular database library

**Answer:**

Python provides several libraries for database operations. The most common approach is using database-specific adapters or ORMs (Object-Relational Mappers).

**Popular Libraries:**

1. **SQLite** (Built-in): `sqlite3` module for SQLite databases
2. **MySQL**: `mysql-connector-python` or `PyMySQL`
3. **PostgreSQL**: `psycopg2` or `psycopg2-binary`
4. **ORM**: `SQLAlchemy` (works with multiple databases)

**Example using `sqlite3` (Built-in):**

```python
import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
''')

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
               ("John Doe", "john@example.com"))
conn.commit()

# Query data
cursor.execute("SELECT * FROM users WHERE name = ?", ("John Doe",))
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()
```

**Example using Context Manager:**

```python
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    # Connection automatically closed
```

**Example using SQLAlchemy (ORM):**

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add user
user = User(name="John Doe", email="john@example.com")
session.add(user)
session.commit()

# Query
users = session.query(User).filter(User.name == "John Doe").all()
session.close()
```

**Best Practices:**
- Use parameterized queries to prevent SQL injection
- Use context managers for automatic connection cleanup
- Handle exceptions appropriately
- Use connection pooling for production applications
- Consider ORMs for complex applications

---

## 27. Explain the concept of virtual environments in Python and their importance

**Answer:**

Virtual environments are isolated Python environments that allow you to install packages separately for different projects, preventing dependency conflicts.

**Why Virtual Environments?**

1. **Dependency Isolation**: Each project can have different package versions
2. **Avoid Conflicts**: Prevents version conflicts between projects
3. **Clean System**: Keeps system Python installation clean
4. **Reproducibility**: Ensures consistent environments across machines
5. **Project Portability**: Easy to share exact dependencies

**Creating Virtual Environments:**

1. **Using `venv` (Python 3.3+, Recommended):**
   ```bash
   python -m venv myenv
   ```

2. **Using `virtualenv` (Third-party, works with Python 2):**
   ```bash
   pip install virtualenv
   virtualenv myenv
   ```

**Activating Virtual Environment:**

- **Linux/Mac:**
  ```bash
  source myenv/bin/activate
  ```

- **Windows:**
  ```bash
  myenv\Scripts\activate
  ```

**Deactivating:**
```bash
deactivate
```

**Working with Virtual Environments:**

```bash
# Create virtual environment
python -m venv project_env

# Activate it
source project_env/bin/activate  # Linux/Mac
# project_env\Scripts\activate  # Windows

# Install packages (only in this environment)
pip install requests numpy

# Generate requirements file
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt

# Deactivate when done
deactivate
```

**Best Practices:**

1. **Always use virtual environments** for projects
2. **One environment per project**
3. **Commit `requirements.txt`** to version control
4. **Don't commit** the virtual environment folder
5. **Use `.gitignore`** to exclude `venv/` or `env/` folders
6. **Recreate environments** from `requirements.txt` for deployment

**Virtual Environment Tools:**

- `venv`: Built-in (Python 3.3+)
- `virtualenv`: Third-party, more features
- `conda`: For data science projects
- `poetry`: Modern dependency management
- `pipenv`: Combines pip and virtualenv

**Example Workflow:**

```bash
# Create project
mkdir my_project
cd my_project

# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate

# Install dependencies
pip install flask requests

# Save dependencies
pip freeze > requirements.txt

# Work on project...
# When done, deactivate
deactivate
```

---

## 28. What is the purpose and usage of the "map" and "filter" functions in Python?

**Answer:**

`map()` and `filter()` are built-in functions that apply operations to iterables in a functional programming style.

**`map()` Function:**

Applies a function to every item in an iterable and returns a map object (iterator).

**Syntax:**
```python
map(function, iterable, ...)
```

**Examples:**

```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# Result: [1, 4, 9, 16, 25]

# Convert to uppercase
words = ['hello', 'world']
upper = list(map(str.upper, words))
# Result: ['HELLO', 'WORLD']

# Multiple iterables
result = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
# Result: [5, 7, 9]
```

**`filter()` Function:**

Filters elements from an iterable based on a function that returns True/False.

**Syntax:**
```python
filter(function, iterable)
```

**Examples:**

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4, 6, 8, 10]

# Filter non-empty strings
words = ['hello', '', 'world', '', 'python']
non_empty = list(filter(None, words))  # None filters falsy values
# Result: ['hello', 'world', 'python']

# Filter by custom condition
ages = [15, 18, 20, 25, 30]
adults = list(filter(lambda x: x >= 18, ages))
# Result: [18, 20, 25, 30]
```

**Key Points:**

1. **Return Iterators**: Both return map/filter objects (iterators), convert to list with `list()`
2. **Lazy Evaluation**: Values computed on-demand
3. **Functional Style**: Encourages functional programming patterns

**Comparison with List Comprehensions:**

```python
# Using map/filter
squared = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Using list comprehension (often preferred)
squared = [x**2 for x in numbers if x % 2 == 0]
```

**When to Use:**

- **`map()`**: Transform each element
- **`filter()`**: Select elements based on condition
- **List Comprehensions**: Often more readable for simple cases
- **`map()`/`filter()`**: Better for functional programming style or when function is already defined

**Best Practices:**

- Use list comprehensions for simple transformations (more Pythonic)
- Use `map()`/`filter()` when function is complex or already defined
- Remember to convert to list if you need a list (not just iteration)
- Can chain `map()` and `filter()` together

---

## 29. How do you perform unit testing in Python using the built-in "unittest" module?

**Answer:**

The `unittest` module provides a testing framework for Python, inspired by JUnit. It supports test automation, sharing setup/teardown code, and test organization.

**Basic Structure:**

```python
import unittest

class TestMathOperations(unittest.TestCase):
    
    def setUp(self):
        # Runs before each test method
        self.calculator = Calculator()
    
    def tearDown(self):
        # Runs after each test method
        pass
    
    def test_addition(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_subtraction(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

**Key Components:**

1. **Test Class**: Inherit from `unittest.TestCase`
2. **Test Methods**: Methods starting with `test_`
3. **Assertions**: Various assert methods to check conditions
4. **Setup/Teardown**: `setUp()` and `tearDown()` for preparation/cleanup

**Common Assertions:**

```python
self.assertEqual(a, b)        # a == b
self.assertNotEqual(a, b)     # a != b
self.assertTrue(x)            # bool(x) is True
self.assertFalse(x)           # bool(x) is False
self.assertIs(a, b)           # a is b
self.assertIsNone(x)          # x is None
self.assertIn(a, b)           # a in b
self.assertRaises(Error)      # Raises specific exception
self.assertAlmostEqual(a, b) # For floating point
```

**Running Tests:**

```bash
# Run all tests in file
python test_file.py

# Run specific test class
python -m unittest TestMathOperations

# Run specific test method
python -m unittest TestMathOperations.test_addition

# Verbose output
python -m unittest -v
```

**Test Organization:**

```python
import unittest

class TestStringMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Runs once before all tests
        pass
    
    @classmethod
    def tearDownClass(cls):
        # Runs once after all tests
        pass
    
    def setUp(self):
        # Runs before each test
        pass
    
    def tearDown(self):
        # Runs after each test
        pass
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

**Best Practices:**

1. **Test Naming**: Use descriptive names starting with `test_`
2. **One Assertion Per Test**: Keep tests focused
3. **Arrange-Act-Assert**: Structure tests clearly
4. **Test Edge Cases**: Include boundary conditions
5. **Mock External Dependencies**: Use `unittest.mock` for isolation
6. **Keep Tests Independent**: Tests shouldn't depend on each other
7. **Use Fixtures**: `setUp()` and `tearDown()` for common setup

**Alternative Testing Frameworks:**

- **pytest**: More Pythonic, simpler syntax
- **nose2**: Extends unittest
- **doctest**: Tests embedded in docstrings

---

## 30. Describe the concept of recursion in Python with an example

**Answer:**

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems.

**Key Concepts:**

1. **Base Case**: Condition that stops recursion (prevents infinite loop)
2. **Recursive Case**: Function calls itself with modified parameters
3. **Call Stack**: Each recursive call adds to the call stack

**Basic Example - Factorial:**

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

**How It Works:**
- `factorial(5)` calls `factorial(4)`
- `factorial(4)` calls `factorial(3)`
- Continues until `factorial(1)` returns 1
- Then unwinds, multiplying results: `5 * 4 * 3 * 2 * 1 = 120`

**Example - Fibonacci Sequence:**

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```

**Example - Binary Search:**

```python
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    # Base case
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
```

**Example - Directory Traversal:**

```python
import os

def list_files(directory):
    files = []
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            files.append(path)
        elif os.path.isdir(path):
            files.extend(list_files(path))  # Recursive call
    return files
```

**Advantages:**
- **Elegant Solutions**: Natural fit for recursive problems (trees, graphs)
- **Readable Code**: Can be more intuitive than iterative solutions
- **Divide and Conquer**: Breaks complex problems into simpler ones

**Disadvantages:**
- **Stack Overflow**: Deep recursion can exceed call stack limit
- **Memory Usage**: Each call uses stack space
- **Performance**: Can be slower than iterative solutions
- **Debugging**: Can be harder to debug

**Tail Recursion:**
Python doesn't optimize tail recursion (recursive call is last operation). For deep recursion, consider iterative solutions or increase recursion limit:

```python
import sys
sys.setrecursionlimit(3000)  # Default is usually 1000
```

**When to Use Recursion:**
- ✅ Tree/graph traversal
- ✅ Divide and conquer algorithms
- ✅ Problems with recursive structure
- ✅ When recursive solution is clearer

**When to Avoid:**
- ❌ Simple iterative solutions available
- ❌ Very deep recursion expected
- ❌ Performance-critical code
- ❌ When iterative solution is clearer

**Best Practices:**
1. Always define a base case
2. Ensure recursive case moves toward base case
3. Consider iterative alternatives for performance
4. Use memoization for repeated subproblems
5. Be mindful of recursion depth limits
