# Context Managers in Python

# Context managers in Python manage the setup and cleanup of resources, like files or network connections, ensuring they are properly handled. 
# They are used with the with statement to ensure resources are acquired and released automatically, even if exceptions occur.

# To create a context manager, a class must implement two special methods:

# 1. **`__enter__(self)`**: 
#       Sets up the resource and returns it.    
#       This method is executed when the flow of control enters the `with` block. It sets up the resource and can return an object to be used within the block.

# 2. **`__exit__(self, exc_type, exc_val, exc_tb)`**: 
#       Cleans up the resource, such as closing a file, and handles exceptions if needed.
#       This method is executed when exiting the `with` block. It is responsible for cleaning up the resource, such as closing a file or a connection. If an exception is raised inside the `with` block, the exception information is passed to `__exit__`.


class File:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f'Opening {self.name}...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing {self.name}...')


if __name__ == '__main__':
    with File('example.txt') as file:
        print(file.name)

    print("Done!")
