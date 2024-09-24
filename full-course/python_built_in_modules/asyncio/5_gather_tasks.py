import asyncio

# gather funtion is a quick way to run multiple coroutines, just like we did manually before.

# So rather than creating task for each coroutine using create_task function, we can simply use gather function and it will
#  automatically run these task concurrently and collect the results in a list in order in which we provide the coroutines


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    # Simulate a network request or IO operation
    await asyncio.sleep(sleep_time)
    # Return some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(
        fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3)
    )

    # Process the results
    for result in results:
        print(f"Received result: {result}")

# Run the main coroutine
asyncio.run(main())


# gather function will not handle exceptions, and is not going to cancel other coroutines if one of them fails.
# which means that you could get some wierd state in your application if you are not handle exceptions manually that could occur.
