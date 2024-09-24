import asyncio


# Semaphores:

# Semaphores work similarly to locks but allow multiple routines to access a resource simultaneously, up to a specified limit (e.g., two routines at a time).

# This is useful for throttling resource usage, such as limiting the number of concurrent network requests to avoid overloading a resource.

# The semaphore ensures that only a defined number of requests are processed simultaneously, preventing overload.


async def access_resource(semaphore, resource_id):
    global shared_resource
    async with semaphore:
        # simulate accessing a limited resource
        print(f"Accessing resource: {resource_id}")
        await asyncio.sleep(1)  # Simulate work with the resource
        print(f"Releasing esource: {resource_id}")


async def main():
    semaphore = asyncio.Semaphore(2)  # allow 2 concurrent accesses
    # creating 5 instances of coruoutine for testing
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

asyncio.run(main())


# *********************************************

# *********************************************
