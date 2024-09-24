import asyncio

# Define a coroutine that simulates a time-consuming task


async def fetch_data(delay, id):
    print(f"Fetching data... id: {id}")
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print(f"Data fetched, id: {id}")
    return {"data": "Some data", "id": id}

# Define another coroutine that calls the first coroutine


async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    # Await the task1 coroutine, pausing execution of main until it completes
    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")

# Run the main coroutine
asyncio.run(main())

# ******************************************

# output:

# Fetching data... id: 1
# Data fetched, id: 1
# Received result: {'data': 'Some data', 'id': 1}
# Fetching data... id: 2
# Data fetched, id: 2
# Received result: {'data': 'Some data', 'id': 2}


# ******************************************

# Uptil this file, we have not find any performance benefit, 
# using await we are just waiting for the task to complete.

# ******************************************
