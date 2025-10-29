# What is asyncio.to_thread?

# It’s a helper in Python’s asyncio library (added in Python 3.9).
# It lets you run a blocking (normal, sync) function in a separate thread without freezing your async event loop.
# Useful when you have CPU-light but blocking I/O tasks (like file reading, database drivers, or requests) inside an async app.


import time
import asyncio


def blocking_task(x):
    # normal blocking function:
    # If you call this directly inside an async function, it will block the event loop.
    print(f"Starting blocking task {x}")
    time.sleep(3)  # Simulates slow work
    print(f"Finished blocking task {x}")
    return x * 2


async def main1():
    print("Before running blocking tasks")

    # Run the blocking function in a background thread
    result1 = await asyncio.to_thread(blocking_task, 5)
    result2 = await asyncio.to_thread(blocking_task, 10)

    print("Results:", result1, result2)
    print("After running blocking tasks")

    # The event loop isn’t blocked 
    # — while your blocking function runs in a separate thread, other async tasks can still run.


# Running Multiple in Parallel
async def main2():
    tasks = [asyncio.to_thread(blocking_task, i) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print("All done:", results)


asyncio.run(main1())
# asyncio.run(main2())
