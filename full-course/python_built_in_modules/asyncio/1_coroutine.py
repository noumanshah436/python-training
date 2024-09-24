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
    
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task

    print(f"Received result: {result}")

    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())


# *****************************

# output:
# python "python_built_in_modules/asyncio/1_coroutine.py"

# Start of main coroutine
# Fetching data...
# Data fetched
# Received result: {'data': 'Some data'}
# End of main coroutine

# *****************************

# coroutine function:
# Any function define with async keyword is a coroutine function and returns a coroutine object


# async def main():
#     print("Start of main coroutine")


# asyncio.run(main())          # main() return a coroutine object

# *****************************
