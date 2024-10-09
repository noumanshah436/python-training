### 2. **`anext()`**

# The `anext()` function is the asynchronous version of `next()` and is used with asynchronous iterators (usually with async generators or any `__anext__()` implementation). 
# This function requires an async context such as `async def` or `await`.

# Example using anext() with an async iterator
import asyncio

class AsyncCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        self.current += 1
        return self.current

async def main():
    async for number in AsyncCounter(1, 5):
        print(number)  # Output: 2, 3, 4, 5 (Each on a new line)
    
    # Manually getting the next item using `anext`
    counter = AsyncCounter(5, 7)
    print(await anext(counter))  # Output: 6
    print(await anext(counter, 'End'))  # Output: 7
    print(await anext(counter, 'End'))  # Output: End

# Run the async function
asyncio.run(main())
