# An async context manager is a special type of context manager that works with asynchronous code.
# In Python, context managers are used with the with statement to handle the setup and cleanup of resources, such as opening and closing files or database connections.
# When working with asynchronous code (for example, code involving async and await), you may need a similar pattern, but for asynchronous operations.

# An async context manager uses __aenter__ and __aexit__ methods instead of __enter__ and __exit__. These methods allow you to await asynchronous tasks, making them compatible with async/await syntax.
# Async context managers are typically used in I/O-bound operations, such as network requests or database queries, where waiting for the operation is required.

import asyncio


class File:
    def __init__(self, name: str):
        self.name = name

    async def __aenter__(self):
        print(f'Opening {self.name}...')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing {self.name}...')


async def main():
    async with File('example.txt') as file:
        print(file.name)

    print("Done!")

# Run the asynchronous code
if __name__ == '__main__':
    asyncio.run(main())


# Explanation:

# 1. **`__aenter__` and `__aexit__`**:
#    - The `__aenter__` method is used to enter the async context. It is similar to `__enter__`, but you can `await` any asynchronous operation (e.g., file I/O or network calls) inside it.
#    - The `__aexit__` method is used to exit the async context. Similarly, it can handle asynchronous cleanup tasks (like closing a network connection or file).

# 2. **Usage**:
#    - The `async with` statement is used to work with async context managers.
#    - Instead of `with`, we use `async with`, and this ensures that we can `await` within the context block if needed.

# 3. **Asynchronous environment**:
#    - We define an asynchronous function `main` that includes the `async with` block.
#    - `asyncio.run(main())` is used to run the async function in an event loop, which allows the program to handle asynchronous tasks.

# When to use async context managers:
# Async context managers are beneficial when the resource you are managing (e.g., file, network connection, or database transaction) involves operations that need to be awaited for non-blocking I/O. For example:
# - Opening and closing async database connections.
# - Managing an asynchronous HTTP client session.
# - Handling long-running tasks asynchronously.
