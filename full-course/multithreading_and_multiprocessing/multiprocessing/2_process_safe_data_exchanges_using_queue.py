"""
How to use a Queue for process safe data exchanges?

Using a Queue from Python's multiprocessing module is one of the safest and most effective ways to exchange data between processes.

✅ Why Use multiprocessing.Queue?
It's process-safe (uses locks and semaphores under the hood)
Allows easy communication between processes (producer-consumer)
Prevents race conditions
Works like queue.Queue from threading, but for separate processes

"""

from multiprocessing import Process, Queue
import time

# Producer function
def producer(q):
    for i in range(5):
        item = f"item-{i}"
        print(f"[Producer] Putting {item}")
        q.put(item)  # Enqueue (process-safe)
        time.sleep(1)

# Consumer function
def consumer(q):
    while True:
        item = q.get()  # Dequeue (blocks until item is available)
        if item is None:
            break  # Sentinel value to stop
        print(f"[Consumer] Got {item}")
        time.sleep(2)

if __name__ == '__main__':
    q = Queue()

    # Create processes
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()     # Wait for producer to finish
    q.put(None)   # Send sentinel to stop consumer
    p2.join()     # Wait for consumer to finish

    print("All tasks completed.")


"""


### 🔍 Key Points

| Line                      | What It Does                              |
| ------------------------- | ----------------------------------------- |
| `q = Queue()`             | Creates a **process-safe** queue          |
| `q.put(item)`             | Safely adds item to the queue             |
| `q.get()`                 | Safely retrieves item from the queue      |
| `q.put(None)`             | Sends a sentinel to tell consumer to stop |
| `p1.join()` / `p2.join()` | Waits for producer and consumer to finish |

---

## 🛠 Real Use Cases

* Worker pools
* Background job processing
* Communication between microservices or subprocesses
* Parallel file or data processing

---

## ✅ Summary

| Feature                       | `multiprocessing.Queue`       |
| ----------------------------- | ----------------------------- |
| Safe for multiple processes   | ✅ Yes                         |
| Avoids race conditions        | ✅ Yes (uses internal locks)   |
| Easy to use                   | ✅ Similar to threading queues |
| Recommended for communication | ✅ Yes                         |

---

Would you like an example using **multiple producers or consumers**, or with a **Manager-based shared list** as well?


"""