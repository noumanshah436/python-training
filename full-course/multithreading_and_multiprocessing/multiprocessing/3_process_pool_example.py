"""
How to use a Process Pool to manage multiple worker processes

Using a Process Pool with Python's multiprocessing.Pool is a powerful way to manage multiple worker processes efficiently — especially when you want to distribute tasks across multiple CPU cores.

✅ What is a Process Pool?
A Process Pool:
Manages a fixed number of worker processes.
Distributes work automatically to free workers.
Handles process creation, task assignment, and termination.
Simplifies parallel execution of tasks.

✅ When to Use It?
Use a Pool when:
You want to parallelize a function over a list of inputs.
You want to process tasks concurrently, but manage them easily.
You're performing CPU-bound tasks (e.g., image processing, math computations).
"""


from multiprocessing import Pool
import time

# Function to run in each process
def square(n):
    print(f"[Worker] Processing {n}")
    time.sleep(1)
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create a pool of 3 worker processes
    with Pool(processes=3) as pool:
        results = pool.map(square, numbers)

    print("Results:", results)


"""


### 🔍 What's Happening:

* `Pool(processes=3)`: Creates 3 worker processes.
* `pool.map(square, numbers)`: Applies the `square` function to each number in the list using the pool — just like Python's built-in `map()` but in parallel.
* `results` will contain the squares of the input numbers.

---

## ✅ Other Useful Pool Methods

| Method                      | Description                                       |
| --------------------------- | ------------------------------------------------- |
| `map(func, iterable)`       | Parallel map. Blocks until all results are ready. |
| `apply(func, args=())`      | Run a single function call in one process.        |
| `apply_async(func)`         | Non-blocking version of `apply()`                 |
| `map_async(func, iterable)` | Non-blocking version of `map()`                   |
| `starmap(func, iterable)`   | Like `map()`, but unpacks each tuple of arguments |

---

## 🧠 Advanced Example — Using `apply_async()`

```python
from multiprocessing import Pool
import time

def work(x):
    print(f"[Worker] Working on {x}")
    time.sleep(2)
    return x * x

def done(result):
    print(f"[Callback] Result received: {result}")

if __name__ == '__main__':
    with Pool(4) as pool:
        for i in range(6):
            pool.apply_async(work, args=(i,), callback=done)

        pool.close()    # No more tasks can be submitted
        pool.join()     # Wait for all tasks to complete

    print("All work completed.")
```

---

## ✅ Summary

| Feature                       | `multiprocessing.Pool`                |
| ----------------------------- | ------------------------------------- |
| Manages worker processes      | ✅ Yes                                 |
| Simplifies parallel execution | ✅ Yes                                 |
| Best for                      | CPU-bound tasks in parallel           |
| Blocking & non-blocking APIs  | ✅ `map()`, `apply()`, `apply_async()` |

---

Would you like an example for **I/O-bound tasks**, **error handling**, or using `concurrent.futures.ProcessPoolExecutor` (more modern alternative)?


"""