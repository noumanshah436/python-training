### 🧠 What Are Descriptors in Python?

A **descriptor** is any object that defines **at least one** of the following special methods:

* `__get__(self, instance, owner)`
* `__set__(self, instance, value)`
* `__delete__(self, instance)`

Descriptors give you **fine-grained control** over attribute access (get, set, delete) on objects.

---

### 🧩 Descriptor Protocol

| Method       | Purpose                               |
| ------------ | ------------------------------------- |
| `__get__`    | Called when the attribute is accessed |
| `__set__`    | Called when the attribute is assigned |
| `__delete__` | Called when the attribute is deleted  |

---

### ✅ Real-Life Example: Type Checking with Descriptors

Let’s build a descriptor that ensures an attribute is always an `int`.

```python
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer")
        instance.__dict__[self.name] = value

class Person:
    age = Integer("age")

    def __init__(self, age):
        self.age = age

p = Person(30)
print(p.age)  # 30
p.age = "hello"  # ❌ Raises: ValueError: age must be an integer
```

---

### 🔍 How It Works

* `Person.age` is an instance of `Integer`, not a regular variable.
* When you do `p.age`, Python calls `Integer.__get__`.
* When you assign `p.age = 40`, it calls `Integer.__set__`.

Python does this automatically when your class attribute is a descriptor.

---

### Types of Descriptors

| Type                    | Definition                         |
| ----------------------- | ---------------------------------- |
| **Data Descriptor**     | Implements `__get__` and `__set__` |
| **Non-Data Descriptor** | Implements only `__get__`          |

Data descriptors **override instance dictionaries**, non-data descriptors **do not**.

---

### 🔄 Built-in Examples Using Descriptors

Python uses descriptors internally in:

* `@property`
* `staticmethod`
* `classmethod`

These are all implemented via descriptors.

```python
class MyClass:
    @property
    def name(self):
        return "Nouman"
```

Here, `property` is a descriptor that defines `__get__`.

---

### 🧾 Summary

| Concept    | Description                                   |
| ---------- | --------------------------------------------- |
| Descriptor | Object controlling attribute access           |
| Use Cases  | Validation, computed properties, lazy loading |
| Real World | Used in `property`, Django models, ORM        |

# *********************************************************


Great! Let’s explore:

---

## ✅ Comparing Descriptors vs. `@property`

### 🔹 Using `@property` (Syntactic Sugar for Descriptors)

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        self._age = value
```

* This is simpler and more **Pythonic** for common use cases.
* Behind the scenes, `@property` creates a **descriptor** with `__get__` and `__set__`.

✅ Use `@property` when:

* The logic is **tied to a single class**.
* You only need **basic** getter/setter behavior.

---

### 🔹 Custom Descriptor (More Powerful)

```python
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Must be an integer")
        instance.__dict__[self.name] = value

class Person:
    age = Integer("age")
    
    def __init__(self, age):
        self.age = age
```

✅ Use descriptors when:

* You want to **reuse logic** across multiple classes.
* You’re building **frameworks**, **ORMs**, or **custom validation tools**.

---

## 🏗️ How Django Models Use Descriptors

Django uses descriptors to handle **model fields** so you can write:

```python
book.title = "Harry Potter"
```

But Django adds a lot of behind-the-scenes logic like:

* Field type checking
* Automatic DB value serialization/deserialization
* Query generation (`Book.objects.filter(title="Harry Potter")`)

### 🔍 Example (Simplified Django-like Field Descriptor):

```python
class Field:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # Add validation, hooks, etc.
        instance.__dict__[self.name] = value

class CharField(Field):
    def __init__(self, name, max_length):
        super().__init__(name)
        self.max_length = max_length

class Model:
    pass

class Book(Model):
    title = CharField("title", max_length=100)

book = Book()
book.title = "The Hobbit"
print(book.title)  # 'The Hobbit'
```

So when Django sees a model class like:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
```

It:

* Uses a **metaclass** to register the field.
* Attaches a **descriptor** (like `CharField`) to manage access.
* Enables behavior like:

  ```python
  book.title  # calls __get__
  book.title = "New Title"  # calls __set__
  ```

---

### ✅ Summary

| Feature        | `@property`                    | Descriptor                                |
| -------------- | ------------------------------ | ----------------------------------------- |
| Simplicity     | Very simple and readable       | More flexible, reusable                   |
| Scope          | Per-class, tied to single attr | Reusable across many classes/attrs        |
| Common Use     | Encapsulation, computed props  | Validation, ORM fields, frameworks        |
| Used in Django | No                             | ✅ Yes — every model field is a descriptor |

---

Would you like to build a mini Django-style model system using metaclasses + descriptors next?
