import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    # Set the result of the future
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def main():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future result is ready"))

    # Wait for the future's result
    result = await future
    print(f"Received the future's result: {result}")

asyncio.run(main())

# **************************************

# ### What a Future is:
# A `Future` is an object that represents a result that will be available at some point in the future. 
# It is essentially a placeholder for a value that will be set once an asynchronous operation completes.

# - **Creating a Future**: In the code, `loop.create_future()` creates a `Future` object.
# - **Setting a Future's Result**: The `future.set_result(value)` method assigns a value to the `Future`, signaling that the asynchronous operation has completed, and the value is now available.
# - **Waiting for the Future's Result**: The code `result = await future` waits until the `Future` has a result set before proceeding.

# In summary, a `Future` is a way of representing an eventual result from an asynchronous operation.

# **************************************

# In this explanation, setting the value of a `Future` and awaiting it means we are simply waiting for a value to 
# become available, not necessarily for the entire task or routine to finish. This is different from using a task, 
# where we wait for the completion of the entire operation. The focus here is on retrieving a value as soon as it's 
# ready, rather than waiting for everything to complete.

# **************************************
