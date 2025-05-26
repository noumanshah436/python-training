Here’s a comprehensive list of **PEP 8 conventions** organized by category to serve as a complete reference guide:

PEP 8 – Style Guide for Python Code (official link):

https://peps.python.org/pep-0008/#introduction

---

### **1. Code Layout**

#### **Indentation**
- Use 4 spaces per indentation level. Avoid tabs.
- Continuation lines should align with the opening delimiter or use a hanging indent.
  ```python
  # Aligned with opening delimiter
  foo = (long_variable_name +
         another_variable)

  # Hanging indent
  foo = (
      long_variable_name
      + another_variable
  )
  ```

#### **Maximum Line Length**
- Limit lines to **79 characters** (72 for docstrings and comments).
- Use parentheses or backslashes to break long lines:
  ```python
  result = some_function(
      arg1, arg2, arg3, arg4
  )
  ```

#### **Blank Lines**
- Use **two blank lines** to separate top-level functions and class definitions.
- Use **one blank line** inside a class to separate methods.
- Separate logical sections of code with blank lines.

---

### **2. Imports**
- Place all imports at the top of the file, right after any module comments and docstrings.
- Follow this order:
  1. Standard library imports.
  2. Related third-party imports.
  3. Local application/library-specific imports.

- Use separate lines for imports:
  ```python
  import os
  import sys
  ```

- Avoid wildcard imports (`from module import *`).

---

### **3. Naming Conventions**

#### **Variables, Functions, and Methods**
- Use **snake_case**:
  ```python
  def calculate_total():
      pass
  ```

#### **Constants**
- Use **UPPERCASE_WITH_UNDERSCORES**:
  ```python
  MAX_RETRIES = 5
  ```

#### **Class Names**
- Use **PascalCase**:
  ```python
  class MyClass:
      pass
  ```

#### **Private Members**
- Prefix private members with a single underscore:
  ```python
  _private_var = 42
  ```

#### **Modules and Packages**
- Use short, lowercase names. Use underscores if necessary:
  ```python
  my_module.py
  ```

---

### **4. String Quotes**
- Use single or double quotes consistently in a file.
- Triple quotes (`"""` or `'''`) for docstrings.

---

### **5. Whitespace**

#### **Spaces Around Operators**
- Use single spaces around operators:
  ```python
  x = 5 + 3
  ```

- Do not use spaces around keyword arguments:
  ```python
  foo(arg=42)
  ```

#### **Spaces in Parentheses, Brackets, or Braces**
- Do not include spaces inside parentheses or brackets:
  ```python
  wrong = ( 1, 2 )
  right = (1, 2)
  ```

#### **Trailing Whitespace**
- Remove unnecessary trailing spaces from lines.

---

### **6. Comments**

#### **Block Comments**
- Explain complex logic or sections of code. Use a leading `#` and a space:
  ```python
  # This function processes the data
  ```

#### **Inline Comments**
- Keep them brief and on the same line, separated by two spaces:
  ```python
  x = x + 1  # Increment counter
  ```

#### **Commenting Out Code**
- Explain why the code is commented out.

---

### **7. Docstrings**
- Use **triple double quotes (`"""`)** for docstrings.
- Provide clear, concise explanations for modules, classes, and functions:
  ```python
  def example():
      """This function does something."""
      pass
  ```

---

### **8. Line Breaks**

#### **Binary Operators**
- Break lines after binary operators for readability:
  ```python
  total = first_number + second_number \
          + third_number
  ```

#### **Avoid Multiple Statements Per Line**
- Use one statement per line:
  ```python
  # Wrong
  x = 1; y = 2

  # Correct
  x = 1
  y = 2
  ```

---

### **9. Exceptions**
- Use specific exception handling instead of a bare `except`:
  ```python
  try:
      value = int(input())
  except ValueError:
      print("Invalid input")
  ```

- Avoid catching too many exceptions.

---

### **10. Classes**

#### **Inheritance**
- If a class has no parent, explicitly inherit from `object` (for Python 2 compatibility):
  ```python
  class MyClass(object):
      pass
  ```

#### **Method Definitions**
- Use `self` for instance methods and `cls` for class methods:
  ```python
  class MyClass:
      def instance_method(self):
          pass

      @classmethod
      def class_method(cls):
          pass
  ```

---

### **11. Type Hints (PEP 484)**
- Use type hints for function arguments and return types:
  ```python
  def add_numbers(a: int, b: int) -> int:
      return a + b
  ```

---

### **12. Testing**
- Write unit tests using the `unittest` module or similar frameworks like `pytest`.
- Use descriptive test method names:
  ```python
  def test_addition_with_positive_numbers():
      pass
  ```

---

### **PEP 8 Tools**
To ensure compliance with PEP 8:
- **flake8**: Linting and style guide enforcement.
- **black**: Auto-formats code to comply with PEP 8.
- **pylint**: Analyzes code for both PEP 8 compliance and logical issues.

Following these conventions ensures Python code is clean, consistent, and maintainable.