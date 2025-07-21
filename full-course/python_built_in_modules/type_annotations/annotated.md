In Python, the `Annotated` type from the `typing` module allows you to add metadata to type hints. This can be useful for providing additional information about the type, which can be used by tools or libraries for various purposes like validation, documentation, or custom processing.

### Basic Usage of `Annotated`

The `Annotated` type allows you to attach metadata to a type annotation, which can be useful for custom processing, documentation, or validation.

```python
from typing import Annotated

def greet(name: Annotated[str, "The name of the person to greet"]) -> None:
    print(f"Hello, {name}!")

greet("Alice")
```

In this example, `"The name of the person to greet"` is a piece of metadata associated with the `str` type annotation for the `name` parameter. This metadata does not affect the type checking but can be used by other tools or libraries to provide additional context.

### Practical Use Cases

#### 1. **Custom Validators**

You can use `Annotated` to attach validation rules or other metadata that can be processed by custom validators or frameworks.

```python
from typing import Annotated
from pydantic import BaseModel, conint

class User(BaseModel):
    age: Annotated[conint(ge=18), "Must be 18 or older"]

user = User(age=20)  # Valid
# user = User(age=17)  # ValidationError
```

In this example, `Annotated` is used to add metadata about the validation rule (`"Must be 18 or older"`) to the `age` field in a `pydantic` model.

#### 2. **Documentation**

Metadata can be used to generate documentation or provide additional information in docstrings.

```python
from typing import Annotated

def calculate_tax(amount: Annotated[float, "The amount to calculate tax on"], rate: Annotated[float, "The tax rate"]) -> float:
    return amount * rate

print(calculate_tax(100.0, 0.05))  # Output: 5.0
```

Here, the metadata provides a description of what each parameter represents, which can be used to generate user-friendly documentation.

#### 3. **Type Alias with Metadata**

You can define type aliases with additional metadata for better code readability and maintenance.

```python
from typing import Annotated, List

# Define a type alias with metadata
PositiveIntegers = Annotated[List[int], "A list of positive integers"]

def sum_positive_numbers(numbers: PositiveIntegers) -> int:
    return sum(numbers)

print(sum_positive_numbers([1, 2, 3]))  # Output: 6
```

In this example, `PositiveIntegers` is a type alias with metadata that specifies the expected content of the list.

### Combining with Other Type Hints

You can use `Annotated` in combination with other type hints to provide more detailed type information.

```python
from typing import Annotated, Dict

# Define a type alias with metadata
Config = Annotated[Dict[str, str], "Configuration settings for the application"]

def load_config(config: Config) -> None:
    print(config)

load_config({"host": "localhost", "port": "8080"})
```

Here, `Config` is a type alias for a dictionary with metadata about its purpose, which can be used for better documentation and understanding of the expected type.

### Summary

- **`Annotated`** allows you to attach metadata to type hints, providing additional context or information about the type.
- **Use cases** include adding validation rules, generating documentation, and creating more readable type aliases.
- **Metadata** does not affect type checking but can be utilized by custom tools, libraries, or documentation generators.

The `Annotated` type helps to enhance the expressiveness of type hints and can be particularly useful in complex projects where additional context or custom processing is required.