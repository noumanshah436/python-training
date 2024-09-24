import asyncio


# Locks: 
# 
# A lock is a synchronization primitive used to ensure that only one coroutine accesses a shared resource at a 
# time. This prevents race conditions, especially in situations like modifying a file or database where concurrent 
# writes can lead to inconsistent states. The async with lock statement checks if a lock is being used by another 
# coroutine and waits for it to finish before proceeding.

# *********************************************

# A shared variable
shared_resource = 0

# An asyncio Lock
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1  # Modify the shared resource
        await asyncio.sleep(1)  # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends


async def main():
    # creating 5 instances of coruoutine for testing
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())


# It still execute coroutines concurrently, but the locked-part can only be accessed by one coroutine a time.

# *********************************************

# ### Code Explanation:

# 1. **Shared Variable**: `shared_resource` is a global variable that multiple tasks will modify.
# 2. **Lock**: `asyncio.Lock()` is used to create a lock object to prevent race conditions when multiple tasks try to modify the shared resource simultaneously.
# 3. **`modify_shared_resource` Function**: This function uses the `async with lock` syntax to ensure only one task can modify the `shared_resource` at a time (i.e., critical section).
# 4. **Main Function**: The `main()` function uses `asyncio.gather()` to run multiple instances of the `modify_shared_resource()` coroutine concurrently. In this case, 5 tasks are created.
# 5. **`asyncio.run(main())`**: This runs the `main()` function within the asyncio event loop.

# This ensures that the shared resource is modified safely across multiple tasks using the asyncio lock mechanism.

# *********************************************
