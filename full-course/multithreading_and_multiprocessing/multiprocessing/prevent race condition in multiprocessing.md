To **prevent race conditions in multiprocessing**, you need to manage **shared resources** using synchronization primitives from Python's `multiprocessing` module — just like you do with threads, but using **process-safe** tools.

---

## 🔥 Why Race Conditions Happen in Multiprocessing

A race condition occurs when **multiple processes**:

* Access and modify shared resources (e.g. counters, files, lists) **without proper coordination**.
* The result depends on the **order/timing of execution**, which can lead to corrupted or unexpected data.

---

## ✅ Tools to Prevent Race Conditions in Multiprocessing

Python provides these **process-safe** tools:

| Tool                      | Description                                                    |
| ------------------------- | -------------------------------------------------------------- |
| `multiprocessing.Lock`    | Ensures only one process accesses a critical section at a time |
| `multiprocessing.Value`   | Shared memory for a single primitive value (e.g., int, float)  |
| `multiprocessing.Array`   | Shared memory for arrays                                       |
| `multiprocessing.Queue`   | Process-safe queue for data exchange                           |
| `multiprocessing.Manager` | Share complex data like dicts/lists between processes          |

---

## ✅ Example: Preventing Race Condition Using `Lock`

```python
from multiprocessing import Process, Value, Lock
import time

def add_100_times(counter, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            counter.value += 1

if __name__ == '__main__':
    counter = Value('i', 0)  # 'i' means integer
    lock = Lock()

    processes = [Process(target=add_100_times, args=(counter, lock)) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"Final counter value: {counter.value}")
```

### 🧠 Explanation:

* `Value('i', 0)`: Shared integer counter (can be read/written by all processes).
* `Lock()`: Ensures that only one process increments the counter at a time.
* `with lock`: Enters a critical section (like a mutex).

---

## ❌ Without the Lock (Race Condition Happens)

If you remove `with lock:`, multiple processes may read and update `counter.value` at the same time, causing missed updates and incorrect results.

---

## ✅ Summary

| Technique           | Use case                                     |
| ------------------- | -------------------------------------------- |
| `Lock`              | Protect critical sections                    |
| `Value` and `Array` | Share primitive types between processes      |
| `Queue`             | Share work or data between processes safely  |
| `Manager`           | Use shared dicts/lists/sets across processes |

---

Would you like an example using `Manager().list()` or `Queue` too?
