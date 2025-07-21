class Integer:
    def __init__(self, name):
        print("Integer init")
        self.name = name

    def __get__(self, instance, owner):
        print("get called")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("set called")
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer")
        instance.__dict__[self.name] = value

class Person:
    age = Integer("age")

    def __init__(self, age):
        print("Person init")
        self.age = age

p = Person(30)
print(p.age)  # 30
# p.age = "hello"  # ❌ Raises: ValueError: age must be an integer