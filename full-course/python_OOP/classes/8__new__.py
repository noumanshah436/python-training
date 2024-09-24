# Class Constructor (__new__):
# The class constructor, also known as the allocator, is responsible for creating a new instance of the class.
# It is a static method that takes the class as its first argument (cls) and returns a new instance of the class.

# It's used less frequently than the __init__ method and is mostly used in cases where you need to customize the object creation process.


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("insile class constructor")
        # Custom object creation process
        instance = super().__new__(cls)
        # Additional customizations if needed
        return instance

    def __init__(self, arg1, arg2):
        print("inside normal constructor")
        self.arg1 = arg1
        self.arg2 = arg2

obj = MyClass(10, 'Hello')
print(obj.arg1)  # Output: 10
print(obj.arg2)  # Output: Hello
