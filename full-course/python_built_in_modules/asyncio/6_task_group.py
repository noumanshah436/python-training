import asyncio


# task group is a slightly more preferred way to create multiple tasks and organize them together. The reason for
# this is that it provides built-in error handling.

# If any of the tasks inside the task group fail, it will automatically cancel all the other tasks, which is typically
#    preferable when dealing with advanced errors or larger applications where we want to be more robust.


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    # Simulate a network request or IO operation
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    # similar to the previous examples, it will run tasks concurrently.
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After the Task Group block, all tasks have completed their execution

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())


# async with  --->  known as asynchronous context manager

# **************************************

# for i, sleep_time in enumerate([2, 1, 3], start=1):
#   print(f"i: {i},  sleep_time:{sleep_time}")

# i: 1,   sleep_time:2
# i: 2,   sleep_time:1
# i: 3,   sleep_time:3

# **************************************

# The task group approach is cleaner and automatically executes all tasks within the group.
# Once all tasks are complete, it stops blocking, allowing the program to continue to the next line of code.
# At that point, the results from the tasks can be retrieved.

# **************************************
