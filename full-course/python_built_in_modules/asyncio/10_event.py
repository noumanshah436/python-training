import asyncio

# Events:

# Events act as simple Boolean flags that enable synchronization in a program.

# By awaiting an event to be set, parts of the code can block execution until the event is marked as true, which is akin to setting a variable.

# In the below example, setter function takes time (2 seconds) to set a result, and execution continues once the event is set.

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")


async def setter(event):
    await asyncio.sleep(2) # simulate doing some work
    event.set()
    print("event has been set")


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())
