import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print("Data fetched")
    return {"data": "Some data"}


# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    print("End of main coroutine")

    # coroutine doesn't start execution until it is awaited or we wrap it in a task which we will practice later.

    result = await task

    print(f"Received result: {result}")


# Run the main coroutine
asyncio.run(main())

#

# output

# Start of main coroutine
# End of main coroutine
# Fetching data...
# Data fetched
# Received result: {'data': 'Some data'}
