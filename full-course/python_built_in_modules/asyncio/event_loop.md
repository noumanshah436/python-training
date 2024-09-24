In Python, the **event loop** is a core concept in `asyncio`, which is Python's library for writing asynchronous code. An event loop is responsible for managing and scheduling asynchronous tasks, executing them as events occur, and coordinating their execution without blocking the program.

Here’s how the event loop works:

1. **Task Scheduling**: When you define asynchronous functions using `async def` and call them using `await`, these functions return coroutines. The event loop schedules these coroutines as tasks.

2. **Execution Management**: The event loop runs these tasks concurrently, switching between them at `await` or I/O-bound operations. However, it doesn't switch them in parallel (like threading); instead, it switches them cooperatively, meaning tasks voluntarily yield control when they reach an `await`.

3. **Non-blocking I/O**: The event loop is highly efficient for I/O-bound tasks like reading from or writing to files, making HTTP requests, or interacting with databases, because it doesn't block on these operations. Instead, it pauses and resumes tasks as the underlying I/O operations complete.

4. **Single Thread**: Although the event loop manages concurrency, it runs on a single thread, meaning it doesn't execute multiple tasks simultaneously (unlike threads or processes). However, it gives the illusion of parallelism by rapidly switching between tasks.

### Basic Example

```python
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)  # Simulates a non-blocking operation
    print("Goodbye!")

# Get the event loop
loop = asyncio.get_event_loop()

# Schedule and run the coroutine
loop.run_until_complete(say_hello())

# Close the loop when done
loop.close()
```

In this example, the event loop runs the coroutine `say_hello()`, which prints "Hello!", pauses for 1 second (non-blocking), and then prints "Goodbye!".

In modern Python, you can also use `asyncio.run()` to simplify this:

```python
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("Goodbye!")

asyncio.run(say_hello())
```

This is equivalent to manually starting and closing the event loop but more concise.

### More than one tasks

```python
import asyncio
import time

async def say1():
    await asyncio.sleep(1)
    print("Hello 1!")

async def say2():
    await asyncio.sleep(1)
    print("Hello 2!")

# Use asyncio.run() to handle the event loop
async def main():
    await asyncio.gather(
        say1(),
        say2()
    )

asyncio.run(main())
```


In summary, the event loop in `asyncio` is the mechanism that drives asynchronous code, managing the scheduling and execution of tasks in a non-blocking manner.