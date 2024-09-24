import asyncio


# Task is a way to schedule a coroutine to run as soon as possible,
#   and allow us to run multiple coroutines simultaneously.

# **************************************************************

# The issue we saw previously is that, we need to wait for one coroutine to finish before we could execute the next.

# With task we don't have that issue.
# When a coroutine is paused or idle, the program switches to another task, optimizing efficiency by always doing work instead of waiting.
# Here we are not using multiple CPU cores, we are just switching from one idle task to start working on another task.

# The whole goal here is that our program is optimizing its efficiency, so we're always attempting to do something. 
#   And when we're waiting on something that's not in control of our program, we switch over to another task.

# **************************************************************

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    # Create tasks for running coroutines concurrently
    # when we create a task, we are scheduling a coroutine to run as quickly as possible.
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))


    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

asyncio.run(main())
